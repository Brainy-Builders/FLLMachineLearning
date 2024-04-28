# FLLMachineLearning
Source code for recording data to train color detection machine learning models on EV3 and Spike Prime kits

## Installation
### For EV3
1. Follow the PyBricks installation guide [here](https://pybricks.com/ev3-micropython/startinstall.html)
2. Install VS Code and the ev3Dev extension
3. Clone this repository in VS Code

### For Spike Prime
1. Create a new **python** Spike Prime project
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
3. move through the options to select the first color you want to train
4. move your robot around slightly while still staying on the color
5. press the stop button once you've got enough data (~1000 entries per color which can be split over multiple readings at multiple times of day and if possible multiple boards)
6. Copy the stuff in between the square brackets into a file with the format ```colorname.json```
7. Repeat with all your colors
## Machine Learning
Upload all your .json files to a google drive folder and open this Google Colab instance
<br>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15q6PGZ2Rg7jCcNPHDlSWeMEhlLRr61Yb?usp=sharing)


