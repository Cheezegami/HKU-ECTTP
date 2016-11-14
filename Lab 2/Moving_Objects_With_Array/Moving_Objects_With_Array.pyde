# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 2.

int_border = 20 # Minimum object distance from edge of the screen.
    
# Specifications of the Rectangle.
int_rWidth = 100  # Object width.
int_rHeight = 100   # Object height.
int_rX = int_border   # Horizontal object position in pixels from the left side of the screen.
int_rY = int_border   # Vertical object position in pixels from the top of the screen.
int_rSpeed = 5   # Amount of pixels the object travels each draw.
bool_rTurnLeft = False # Moving an object along the X axis.
bool_rTurnDown = False # Moving an object along the Y axis.

#Specifications of the Ellipse.
int_eWidth = 100   # Object width.
int_eHeight = 100   # Object height.
int_eX = int_border   # Horizontal object position in pixels from the left side of the screen.
int_eY = int_border    # Vertical object position in pixels from the top of the screen.
int_eSpeed = 10   # Amount of pixels the object travels each draw.
bool_eTurnLeft = False # Moving an object along the X axis.
bool_eTurnDown = False # Moving an object along the Y axis.

int_oWidth = [100,100]
int_oHeight = [100,100]
int_oX = [int_border+250,int_border+250]
int_oY = [int_border,int_border+250]
int_oSpeed = [2,12]
bool_oTurnLeft = [False,False]
bool_oTurnDown = [False,False]

int_errorMargin = int_border + max(max(int_oWidth),max(int_oHeight),max(int_oWidth),max(int_oHeight)) + 50 # Defining what's the minimal parameter required for an error message about the window size being to small to pop up.
def setup(): # Defining parameters that run once.
    size(1000,500)
    global int_eX
    int_eX = width - int_eWidth - int_border
    background(255) # A white background.
    ellipseMode(CORNER) # My calculations are based on the upper left corner of the ellipse.

def draw(): # Continually runs as long as the program runs.
    global int_rX
    global int_rY
    global int_rSpeed
    global int_eX
    global int_eY
    global int_eSpeed
    global int_oX
    global int_oY
    global int_oSpeed
    global int_border
    global int_errorMargin
    
    global bool_eTurnLeft
    global bool_eTurnDown
    global bool_rTurnLeft
    global bool_rTurnDown
    global bool_oTurnLeft
    global bool_oTurnDown
    
    calculateDirection(int_oX,int_oY,int_oSpeed,int_border,int_oWidth,int_oHeight,bool_oTurnLeft,bool_oTurnDown) # Moving the Rectangle
    
    background(255)
    fill(255,127,60)
    ellipse(int_oX[0],int_oY[0],int_oWidth[0],int_oHeight[0])
    fill(60,127,255)
    rect(int_oX[1],int_oY[1],int_oWidth[1],int_oHeight[1])
    if(width <= int_errorMargin or height <= int_errorMargin) : # Giving an error when the window is too small for the objects to move on.
        print("The window size is too small, make sure both the width:(", width ,") and the height:(", height ,") of the window are bigger than ", int_errorMargin ,"for the optimal screen traversing experience!")


def calculateDirection(int_oX,int_oY,int_oSpeed,int_border,int_oWidth,int_oHeight,bool_oTurnLeft,bool_oTurnDown) : # Moving the Rectangle.
        # Horizontal
        for i in range(0,len(int_oSpeed)) :
            if(bool_oTurnLeft[i] == False) : # Make Object go Right.
             int_oX[i] += int_oSpeed[i]
             if(int_oX[i] >= width-int_oWidth[i]-int_border) :
                bool_oTurnLeft[i] = True
            else :                           # Make Object go Left.
              int_oX[i] -= int_oSpeed[i]
              if(int_oX[i] <= 0+int_border) :
                bool_oTurnLeft[i] = False
        # Vertical
            if(bool_oTurnDown[i] == False) : # Make Object go Down.
             int_oY[i] += int_oSpeed[i]
             if(int_oY[i] >= height-int_oHeight[i]-int_border) :
                bool_oTurnDown[i] = True
            else :                        # Make Object go Up.
             int_oY[i] -= int_oSpeed[i]
             if(int_oY[i] <= 0+int_border) :
                bool_oTurnDown[i] = False
        print("Object",i,"xPosition:", int_oX[i],bool_oTurnLeft[i],"yPosition:", int_oY[i],bool_oTurnDown[i])