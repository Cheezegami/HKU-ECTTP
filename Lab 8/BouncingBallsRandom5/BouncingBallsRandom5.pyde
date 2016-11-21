# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 8.
# Known Bugs: Objects can get stuck when colliding : Fix this by moving the movable rectangle over them, that will make them go unstuck.

# Importing the GenericObject class.
from GenericObject import GenericObject
from ScoreBoard import ScoreBoard
# Variable to store objects.
objectList = [] # Array in which the objects are contained.
score = ScoreBoard()
# Creating variables.
int_border = 0 # Minimum object distance from edge of the screen.
int_bgColor = 50 # Background color.
def setup(): # Defining parameters that run once.
    size(1400,800) # Screen size. (Width,Height)
    # Object Creation.
    #Speed, Shape, Movestyle, Red, Green, Blue, Border.
    objectList.append(GenericObject(25+random(50),25+random(50),int_border+random(width-int_border),+random(height-int_border),2+random(5),"rectangle",0,60,127,255,int_border)) # First Object, bouncing rectangle.
    for i in range (0,10):
        int_size = 25+ random(50)
        objectList.append(GenericObject(int_size,int_size,int_border+random(width-int_border),int_border+random(height-int_border),2+random(5),"ellipse",0,255,127,60,int_border)) # Second Object, bouncing ellipse.
    objectList.append(GenericObject(150,100,int_border+random(width-int_border),int_border+random(height-int_border),2+10,"rectangle",1,127,60,255,int_border)) # Third, Movable Object
    #objectList.append(GenericObject(100,100,int_border+random(width-int_border),int_border+random(height-int_border),10,"ellipse",2,127,60,255,int_border)) # Fourth, Time Based Object.
    
    background(int_bgColor) # Set up background.
    noStroke() # No outer edge on objects
    GenericObject.setupGenericObject() # Sets up parameters needed by GenericObject.
    
def draw(): # Continually runs as long as the program runs.
    background(int_bgColor) # Cleaning the screen from previous draws.
    for i in range(0, len(objectList)) : # For loop based on total number of objects
        GenericObject.update(objectList[i]) # Run the methods in the GenericObject class responsible for defining the position and drawing the objects.
        for k in range(i, len(objectList)):
            if(i != k):
                objectList[i].checkCollision(objectList[k])
    ScoreBoard.update(score)