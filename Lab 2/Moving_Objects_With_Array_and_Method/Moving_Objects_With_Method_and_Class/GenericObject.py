class GenericObject(object) :
    def __init__(self,int_oWidth,int_oHeight,int_oX,int_oY,int_border,int_oSpeed,bool_oTurnLeft,bool_oTurnUp,String_form) : # Constructor
        self.int_oWidth = int_oWidth
        self.int_oHeight = int_oHeight
        self.int_oX = int_oX
        self.int_oY = int_oY
        self.int_border = int_border
        self.int_oSpeed = int_oSpeed
        self.bool_oTurnLeft = bool_oTurnLeft
        self.bool_oTurnUp = bool_oTurnUp
        self.String_form = String_form
        
    @staticmethod
    def setupGenericObject() :
        ellipseMode(CORNER) # My calculations are based on the upper left corner of the ellipse.
    
    def update(self):
        self.printError()
        if(self.String_form == "ellipse") :
            self.drawEllipse(self.int_oWidth,self.int_oHeight,self.int_oX,self.int_oY)
        elif(self.String_form == "rectangle") :
            self.drawRectangle(self.int_oWidth,self.int_oHeight,self.int_oX,self.int_oY)
        else :
            print(self, "is missing a shape")
        self.calculateDirection()
        #print(self.int_oWidth,self.int_oHeight,self.int_oX,self.int_oY,self.int_oSpeed,self.int_border,self.bool_oTurnLeft,self.bool_oTurnUp,"Test")

        
    def calculateDirection(self) : # Method for moving the Objects.
        # Horizontal
        if(self.bool_oTurnLeft == False) :    # Make Object go Right.
           self.int_oX += self.int_oSpeed
           if(self.int_oX >= width-self.int_oWidth-self.int_border) :   # If reached the right edge turn left.
              self.bool_oTurnLeft = True
              print("Check_1")
        else :                           # Make Object go Left.
           self.int_oX -= self.int_oSpeed
           if(self.int_oX <= 0+self.int_border) :                     # If reached the left edge turn right.
              self.bool_oTurnLeft = False
              print("Check_2")
        # Vertical
        if(self.bool_oTurnUp == False) :      # Make Object go Up.
           self.int_oY += self.int_oSpeed
           if(self.int_oY >= height-self.int_oHeight-self.int_border) : # If reached the bottom edge turn up.
              self.bool_oTurnUp = True
              print("Check_3")
        else :                           # Make Object go Up.
           self.int_oY -= self.int_oSpeed
           if(self.int_oY <= 0+self.int_border) :                     # If reached the top edge turn down.
              self.bool_oTurnUp = False
              print("Check_4")
        print("Object",self,"xPosition:", self.int_oX,self.bool_oTurnLeft,"yPosition:", self.int_oY,self.bool_oTurnUp) # Printing Object Number, Position on the X axis, Whether Object Going Left or not, Position on the Y axis, Whether Object Going Up or not.
        
    def printError(self) :
        int_errorMargin = self.int_border + max(self.int_oWidth,self.int_oHeight) + 50 # Defining what's the minimal parameter required for an error message about the window size being to small to pop up.
        if(width <= int_errorMargin or height <= int_errorMargin) : # Giving an error when the window is too small for the objects to move on.
           print("The window size is too small, make sure both the width:(", width ,") and the height:(", height ,") of the window are bigger than ", int_errorMargin ,"for the optimal screen traversing experience!") # Printing the error to the console.
           
    def drawRectangle(self,int_oWidth,int_oHeight,int_oX,int_oY) :
        fill(255,127,60)
        rect(int_oX,int_oY,int_oWidth,int_oHeight)
        
    def drawEllipse(self,int_oWidth,int_oHeight,int_oX,int_oY) :
        fill(60,127,255)
        ellipse(int_oX,int_oY,int_oWidth,int_oHeight)
    