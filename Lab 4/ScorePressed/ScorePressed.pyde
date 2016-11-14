# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 3.

# Importing the GenericObject class.
from GenericObject import GenericObject
from ScoreBoard import ScoreBoard
from ObjectRunner import ObjectRunner
# Variable to store objects.
score = ScoreBoard(0)
object = ObjectRunner()
# Creating variables.
int_border = 0 # Minimum object distance from edge of the screen.
int_bgColor = 50 # Background color.
def setup(): # Defining parameters that run once.
    size(1400,700) # Screen size. (Width,Height)
    background(int_bgColor) # Set up background.
    noStroke() # No outer edge on objects
    ObjectRunner.createObjects(object) # Create the objects.
    GenericObject.setupGenericObject() # Sets up parameters needed by GenericObject.
    
def draw(): # Continually runs as long as the program runs.
    background(int_bgColor) # Cleaning the screen from previous draws.
    for i in range(0, len(ObjectRunner.objectList)) : # For loop based on total number of objects
        GenericObject.update(ObjectRunner.objectList[i]) # Run the methods in the GenericObject class responsible for defining the position and drawing the objects.
    ScoreBoard.update(score)