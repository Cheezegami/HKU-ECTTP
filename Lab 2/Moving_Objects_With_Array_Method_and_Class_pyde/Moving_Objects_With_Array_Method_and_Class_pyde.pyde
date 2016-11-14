# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 2.

# Importing the GenericObject class.
from GenericObject import GenericObject
from MovableObject import MovableObject

# Variable to store objects.
objectList = [] # Array in which the objects are contained.

# Creating variables.
int_border = 0 # Minimum object distance from edge of the screen.
int_bgColor = 50 # Background color.
                    
def setup(): # Defining parameters that run once.
    size(1400,700) # Screen size. (Width,Height)
    # Object Creation.
    # Width, Height, X, Y, Border, Speed, Going Left, Going Up, Shape.
    objectList.append(GenericObject(50,50,int_border+random(width-int_border),+random(height-int_border),int_border,5,False,False,"rectangle")) # First Object
    objectList.append(GenericObject(100,100,int_border+random(width-int_border),int_border+random(height-int_border),int_border,10,False,False,"ellipse")) # Second Object
    objectList.append(MoveableObject(100,100,int_border+random(width-int_border),int_border+random(height-int_border),int_border,10,False,False,"ellipse")) # Third, Movable Object
    background(int_bgColor) # Set up background.
    noStroke() #No outer edge on objects
    GenericObject.setupGenericObject()
    
def draw(): # Continually runs as long as the program runs.
    background(int_bgColor) # Cleaning the screen from previous draws.
    for i in range(0, len(objectList)) : # For loop based on total number of objects
        GenericObject.update(objectList[i]) # Run the methods in the GenericObject class responsible for defining the position and drawing the objects.