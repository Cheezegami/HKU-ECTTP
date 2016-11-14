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
        if(self.String_form == "ellipse") : # If an ellipse draw an ellipse.
            self.drawEllipse(self.int_oWidth,self.int_oHeight,self.int_oX,self.int_oY)
        elif(self.String_form == "rectangle") : # If a rectangle draw a rectangle.
            self.drawRectangle(self.int_oWidth,self.int_oHeight,self.int_oX,self.int_oY)
        else : # If no shape or having a invalid shape.
            print(self, "is missing a shape or having an invalid shape.")
        self.calculateDirection()
        #print(self.int_oWidth,self.int_oHeight,self.int_oX,self.int_oY,self.int_oSpeed,self.int_border,self.bool_oTurnLeft,self.bool_oTurnUp,"Test") # Debugging.

        
    def calculateDirection(self) : # Method for moving the Objects.
        # Horizontal
        bool_listDirection =  [self.bool_oTurnLeft,self.bool_oTurnLeft]
        bool_listSize = [width,height]
        int_listObjectPosition = [self.int_oWidth,self.int_oHeight]
        int_list = [self.int_oX,self.int_oY]
        for i in range (0,len(bool_listDirection)) :
            if(bool_listDirection[i] == False) :    # Make Object go Right.
                int_list[i] += self.int_oSpeed
                if(int_list[i] >= bool_listSize[i]-int_listObjectPosition[i]-self.int_border) :   # If reached the right edge turn left.
                    bool_listDirection[i] = True
                    print("Check_1")
            else :                           # Make Object go Left.
                int_list[i] -= self.int_oSpeed
                if(int_list[i] <= 0+self.int_border) :                       # If reached the left edge turn right.
                    bool_listDirection[i] = False
                    print("Check_2")
            if(i == 0) :
                self.int_oX = int_list[i]
                self.bool_oTurnLeft = bool_listDirection[i]
            else :
                self.int_oY = int_list[i]
                self.bool_oTurnUp = bool_listDirection[i]
                
        # Vertical
        #if(self.bool_oTurnUp == False) :      # Make Object go Up.
        #   self.int_oY += self.int_oSpeed
        #   if(self.int_oY >= height-self.int_oHeight-self.int_border) : # If reached the bottom edge turn up.
        #      self.bool_oTurnUp = True
        #      print("Check_3")
        #else :                           # Make Object go Up.
        #   self.int_oY -= self.int_oSpeed
        #   if(self.int_oY <= 0+self.int_border) :                       # If reached the top edge turn down.
        #      self.bool_oTurnUp = False
        #      print("Check_4")
        print("Object",self,"xPosition:", self.int_oX,self.bool_oTurnLeft,"yPosition:", self.int_oY,self.bool_oTurnUp) # Printing Object Number, Position on the X axis, Whether Object Going Left or not, Position on the Y axis, Whether Object Going Up or not.
        
    def printError(self) : # A method to check errors.
        int_errorMargin = self.int_border + max(self.int_oWidth,self.int_oHeight) + 50 # Defining what's the minimal parameter required for an error message about the window size being to small to pop up.
        if(width <= int_errorMargin or height <= int_errorMargin) : # Giving an error when the window is too small for the objects to move on.
           print("The window size is too small, make sure both the width:(", width ,") and the height:(", height ,") of the window are bigger than ", int_errorMargin ,"for the optimal screen traversing experience!") # Printing the error to the console.
           
    def drawRectangle(self,int_oWidth,int_oHeight,int_oX,int_oY) : # A method to draw Rectangles.
        fill(255,127,60) # As of right now all rectangles are orange.
        rect(int_oX,int_oY,int_oWidth,int_oHeight) # Rectangle
        
    def drawEllipse(self,int_oWidth,int_oHeight,int_oX,int_oY) : #  A method to draw Ellipses.
        fill(60,127,255) # As of right now all ellipses are blue.
        ellipse(int_oX,int_oY,int_oWidth,int_oHeight) # Ellipse
    