# FLLMachineLearning
Source code for recording data to train color detection machine learning models on EV3 and Spike Prime kits

## Installation
### For EV3
1. Follow the PyBricks installation guide [here](https://pybricks.com/ev3-micropython/startinstall.html)
2. Install [VS Code](https://code.visualstudio.com/) and the [ev3Dev extension](https://marketplace.visualstudio.com/items?itemName=ev3dev.ev3dev-browser)
3. Clone this repository in VS Code

### For Spike Prime
1. Create a new **python** [Spike Prime project](https://spike.legoeducation.com/prime/lobby)
2. Clone this repository to your computer
3. Copy the contents of **main.py** to the project

### Editing the project
4. Remove the pybricks shebang if you are using spike prime
```python
#!/usr/bin/env pybricks-micropython
```
5. edit ```sensorsToCheck``` to include the ones you use
6. edit ```trainableColors``` to include color options 
## Usage
1. Run the project
2. Check the EV3 screen or Spike Prime console for instructions
3. Place your color sensors on the first color
4. move through the options to select the first color you want to train
5. move your robot around slightly while still staying on the color
6. press the stop button once you've got enough data (~1000 entries per color which can be split over multiple readings at multiple times of day and if possible multiple boards)
7. Copy the stuff in between the square brackets into a file with the format ```colorname.json```
ie.
```javascript
[{"id": "Port.S1", "reflectivity": 13, "truth": "Black", "blue": 10, "classification": "Black", "ambient": -73, "red": 12, "green": 13}, {"id": "Port.S1", "reflectivity": 12, "truth": "Black", "blue": 9, "classification": "Black", "ambient": 1, "red": 11, "green": 12},...]
```
8. Repeat with all your colors
## Machine Learning
Upload all your .json files to a google drive folder and open this Google Colab instance
<br>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15q6PGZ2Rg7jCcNPHDlSWeMEhlLRr61Yb?usp=sharing)


# License 
## **Boost Software License 1.0**
You can redistribute, reproduce, modify, and sell this software as long as you also use the BSL license and give some credit