# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 2.

# Importing the GenericObject class.
from GenericObject import GenericObject
int_border = 0 # Minimum object distance from edge of the screen.

# Object Creation.
# Width, Height, X, Y, Border, Speed, Going Left, Going Right, Shape.
object_1 = GenericObject(50,50,int_border+250,int_border,int_border,5,False,False,"rectangle") # First Object
object_2 = GenericObject(100,100,int_border,int_border+250,int_border,10,False,False,"ellipse") # Second Object
                        
def setup(): # Defining parameters that run once.
    size(1000,700) # Screen size.
    background(50) # A g background.
    noStroke()
    GenericObject.setupGenericObject()
    
def draw(): # Continually runs as long as the program runs.
    background(50) # Cleaning the screen from previous draws.
    GenericObject.update(object_1)
    GenericObject.update(object_2)