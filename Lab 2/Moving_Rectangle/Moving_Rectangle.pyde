
int_border = 20 # Distance from edge of the screen.

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
int_eX = 0   # Horizontal object position in pixels from the left side of the screen.
int_eY = int_border    # Vertical object position in pixels from the top of the screen.
int_eSpeed = 10   # Amount of pixels the object travels each draw.
bool_eTurnLeft = False # Moving an object along the X axis.
bool_eTurnDown = False # Moving an object along the Y axis.


def setup(): # Defining parameters that run once.
    size(1000,800)
    global int_eX
    int_eX = width - int_eWidth - int_border
    
    background(255)
    ellipseMode(CORNER)

def draw(): # Continually runs as long as the program runs.
    global int_rX
    global int_rY
    global int_rSpeed
    global int_eX
    global int_eY
    global int_eSpeed
    global int_border
    global bool_eTurnLeft
    global bool_eTurnDown
    global bool_rTurnLeft
    global bool_rTurnDown
    
    if(bool_rTurnLeft == False) : # Make Object go Right
        int_rX += int_rSpeed
        if(int_rX >= width-int_rWidth-int_border) :
            bool_rTurnLeft = True
    else : #Make Object go Left.
        int_rX -= int_rSpeed
        if(int_rX <= 0+int_border) :
            bool_rTurnLeft = False
    
    if(bool_rTurnDown == False) : # Make Object go Down
        int_rY += int_rSpeed
        if(int_rY >= height-int_rHeight-int_border) :
            bool_rTurnDown = True
    else : # Make Object go Up.
        int_rY -= int_rSpeed
        if(int_rY <= 0+int_border) :
            bool_rTurnDown = False
    
    
    
    if(bool_eTurnLeft == False) : # Make Object go Right
        int_eX += int_eSpeed
        if(int_eX >= width-int_eWidth-int_border) :
            bool_eTurnLeft = True
    else : #Make Object go Left.
        int_eX -= int_eSpeed
        if(int_eX <= 0+int_border) :
            bool_eTurnLeft = False
    
    if(bool_eTurnDown == False) : # Make Object go Down
        int_eY += int_eSpeed
        if(int_eY >= height-int_eHeight-int_border) :
            bool_eTurnDown = True
    else : # Make Object go Up.
        int_eY -= int_eSpeed
        if(int_eY <= 0+int_border) :
            bool_eTurnDown = False
    
    print("Ellipse xPosition:", int_eX,bool_eTurnLeft,"Ellipse yPosition:", int_eY,bool_eTurnDown)
    print("Rectangle xPosition:", int_rX,bool_rTurnLeft,"Rectangle yPosition:", int_rY,bool_rTurnDown)
    background(255)
    fill(255,127,60)
    ellipse(int_eX,int_eY,int_eWidth,int_eHeight)
    fill(60,127,255)
    rect(int_rX,int_rY,int_rWidth,int_rHeight)
    
            