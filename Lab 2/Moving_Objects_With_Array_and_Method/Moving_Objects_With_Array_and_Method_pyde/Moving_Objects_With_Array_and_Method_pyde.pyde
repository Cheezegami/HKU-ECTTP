# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 2.

int_border = 0 # Minimum object distance from edge of the screen.
    
#Specifications of the Objects.
#0 = Ellipse.
#1 = Rectangle.
int_oWidth = [50,50]
int_oHeight = [50,50]
int_oX = [int_border+250,int_border+250]
int_oY = [int_border,int_border+200]
int_oSpeed = [5,10]
int_backgroundShade = 50
bool_oTurnLeft = [False,False]
bool_oTurnUp = [False,False]

int_errorMargin = int_border + max(max(int_oWidth),max(int_oHeight),max(int_oWidth),max(int_oHeight)) + 50 # Defining what's the minimal parameter required for an error message about the window size being to small to pop up.
def setup(): # Defining parameters that run once.
    size(1250,750) # Screen size.
    noStroke() # No Borders to Objects.
    background(int_backgroundShade) # A grey background.
    ellipseMode(CORNER) # My calculations are based on the upper left corner of the ellipse.

def draw(): # Continually runs as long as the program runs.
    global int_oX # Loading Integers
    global int_oY
    global int_oSpeed
    global int_border
    global int_errorMargin
    global bool_oTurnLeft # Loading Booleans
    global bool_oTurnUp
    
    calculateDirection(int_oX,int_oY,int_oSpeed,int_border,int_oWidth,int_oHeight,bool_oTurnLeft,bool_oTurnUp) # Moving the Objects.
    
    background(int_backgroundShade) # Preventing the objects from leaving a trail.
    fill(255,127,60) # Orange
    ellipse(int_oX[0],int_oY[0],int_oWidth[0],int_oHeight[0]) # Drawing an Ellipse with parameters from calculateDirection.
    fill(60,127,255) # Blue
    rect(int_oX[1],int_oY[1],int_oWidth[1],int_oHeight[1]) # Drawing a Rectangle with parameters from calculateDirection.
    if(width <= int_errorMargin or height <= int_errorMargin) : # Giving an error when the window is too small for the objects to move on.
        print("The window size is too small, make sure both the width:(", width ,") and the height:(", height ,") of the window are bigger than ", int_errorMargin ,"for the optimal screen traversing experience!") # Printing the error to the console.


def calculateDirection(int_oX,int_oY,int_oSpeed,int_border,int_oWidth,int_oHeight,bool_oTurnLeft,bool_oTurnUp) : # Method for moving the Objects.
        # Horizontal
        for i in range(0,len(int_oSpeed)) :
            if(bool_oTurnLeft[i] == False) : # Make Object go Right.
             int_oX[i] += int_oSpeed[i]
             if(int_oX[i] >= width-int_oWidth[i]-int_border) :   # If reached the right edge turn left.
                bool_oTurnLeft[i] = True
            else :                           # Make Object go Left.
              int_oX[i] -= int_oSpeed[i]
              if(int_oX[i] <= 0+int_border) :                    # If reached the left edge turn right.
                bool_oTurnLeft[i] = False
        # Vertical
            if(bool_oTurnUp[i] == False) : # Make Object go Up.
             int_oY[i] += int_oSpeed[i]
             if(int_oY[i] >= height-int_oHeight[i]-int_border) : # If reached the bottom edge turn up.
                bool_oTurnUp[i] = True
            else :                        # Make Object go Up.
             int_oY[i] -= int_oSpeed[i]
             if(int_oY[i] <= 0+int_border) :                     # If reached the top edge turn down.
                bool_oTurnUp[i] = False
            print("Object",i,"xPosition:", int_oX[i],bool_oTurnLeft[i],"yPosition:", int_oY[i],bool_oTurnUp[i]) # Printing Object Number, Position on the X axis, Whether Object Going Left or not, Position on the Y axis, Whether Object Going Up or not.