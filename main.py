#!/usr/bin/env pybricks-micropython

#          Copyright Brainy Builders 2024.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)


try: # we test to see if we are on SPIKE or EV3
    import hub
    from hub import button
    import color_sensor
    import color as Color # cast it's name so it matches the same case as ev3
    from hub import port
    useSpike = True
except ImportError:
    import pybricks
    from pybricks.hubs import EV3Brick  
    from pybricks.parameters import Port, Button, Color
    from pybricks.media.ev3dev import Font #for Display
    from pybricks.ev3devices import ColorSensor
    big_font = Font(size=14, bold=True) # A big font to choose color
    ev3 = EV3Brick()
    
    useSpike = False

import ujson as json
import time # time is universal

sensorsToCheck = [Port.S1] # You fill this in with which sensors are connected docs are here (ev3: https://pybricks.com/ev3-micropython/parameters.html#pybricks.parameters.Port, spikePrime: https://spike.legoeducation.com/prime/modal/help/lls-help-python#lls-help-python-spm-hub-port)
# If you want do do spike, it would be something like this:
# port.A, port.B, etc...


#Print Statements
if useSpike:
    menuPrint = print # when we do menu selection we log it to the console on spike, because it lacks a display

    #We have a universal definition of button pressed
    isLeftPressed = lambda: button.pressed(button.LEFT)
    isRightPressed = lambda: button.pressed(button.RIGHT)
else: 
    menuPrint = ev3.screen.print
    ev3.screen.set_font(big_font)

    isLeftPressed = lambda: Button.LEFT in ev3.buttons.pressed()
    isRightPressed = lambda: Button.RIGHT in ev3.buttons.pressed()



class Other: # Create an "other" class to match the match the other colors
    def __str__(self) -> str:
        return "Color.Other"
    def __repr__(self) -> str:
        return "Color.Other"

trainableColors = [
    Color.BLACK, Color.WHITE, Other()
] # What colors do you want to train on, For us we use White, Black, and Other (See here for colors: https://spike.legoeducation.com/prime/modal/help/lls-help-python#lls-help-python-spm-color)

def select():
    '''
    A function that polls the left and right buttons and uses it to select a color from trainableColors list based on user input
    Returns:
        color: A value from trainableColors
    '''
    currentIndex = 0
    menuPrint("Starting with\n", str(trainableColors[currentIndex]))
    while True:
        time.sleep(0.2) # We don't want to lag out the system (You may need to be patient for the button presses to register)
        if (isLeftPressed()):
            return trainableColors[currentIndex] # When you press left, we return color
        if (isRightPressed()):
            currentIndex+=1 # The right button cycles through the color
            currentIndex = currentIndex % len(trainableColors)
            menuPrint("Selected color: \n", trainableColors[currentIndex]) # Show the new selected color

def getColorData(port, trainingColor):
    '''
    Get the color data into a trainable format regardless of the hub type
    Parameters:
        port: The EV3 or Spike port that is used to read color sensor data from
    Returns:
        data: A dictionary containing data extracted from the port
    '''
    if useSpike:
        red, green, blue, ambient = color_sensor.rgbi(port) # Get RGB and ambient light from the spike prime sensor
        reflectivity = color_sensor.reflection(port) # Get reflection of the sensor
        colorEstimate = color_sensor.color(port) # get what spike thinks the color is (Not accurate why were doing the machine learning in the first place)
    else:
        ev3sensor = ColorSensor(port)
        red, green, blue = ev3sensor.rgb() # Get RGB from the ev3 sensor
        ambient = ev3sensor.ambient() # Get ambient light intensity from the ev3 sensor
        reflectivity = ev3sensor.reflection() # Get reflective intensity from the ev3 sensor
        colorEstimate = ev3sensor.color() # Get what ev3 thinks the color is

    return {
        'id': str(port),
        'red': red,
        'green': green,
        'blue': blue,
        'ambient': ambient,
        'reflectivity': reflectivity,
        'classification': str(colorEstimate).replace("Color.",""),
        'truth': str(trainingColor).replace("Color.","")
    }

def main():
    menuPrint("Brainy Builders\n Machine Learning \nData Acquisition \nprogram loading...")
    colorToTrain = select() # See the above function
    menuPrint("Press left\n button to stop")
    menuPrint("Starting in\n 5 secs")

    dataList = [] # Store all the data entries
    time.sleep(5)
    menuPrint("Go")
    while True:
        if (isLeftPressed()): break # Stop collecting data
        for sensor in sensorsToCheck:
            if (len(dataList)%10 == 0):
                menuPrint("{} Data entries".format(len(dataList))) # Tell us how many entries we've recorded so far
            sensorData = getColorData(sensor, colorToTrain)
            dataList.append(sensorData) # Add our collected data to the list
    print(json.dumps(dataList)) # print out all the data entries



main()