from ScoreBoard import ScoreBoard

class Ball(object) :
    def __init__(self, int_oX,int_oY,int_oWidth,int_oHeight,int_oSpeed,int_border): #constructor
        self.int_oX = int_oX
        self.int_oY = int_oY
        self.int_oWidth = int_oWidth
        self.int_oHeight = int_oHeight
        self.int_oSpeed = int_oSpeed
        self.int_border = int_border
        self.bool_oTurnLeft = False
        self.bool_oTurnUp = False
        
    def update(self):
        self.moveDirection()
        self.drawShape()
        self.screenBorder()
        
    
    def moveDirection(self) : # Method for moving the Objects.
        # Horizontal
        if(self.bool_oTurnLeft == False) :                              # Make Object go Right.
            self.int_oX += self.int_oSpeed
            if(self.int_oX >= width-self.int_oWidth-self.int_border) :   # If reached the right edge turn left.
                self.bool_oTurnLeft = True
                print("Check_Right")
        else :                                                          # Make Object go Left.
            self.int_oX -= self.int_oSpeed
            if(self.int_oX <= 0+self.int_border) :                       # If reached the left edge turn right.
                self.bool_oTurnLeft = False
                print("Check_Left")
        # Vertical
        if(self.bool_oTurnUp == False) :                                # Make Object go Down.
           self.int_oY += self.int_oSpeed
           if(self.int_oY >= height-self.int_oHeight-self.int_border) : # If reached the bottom edge turn down.
              self.bool_oTurnUp = True
              print("Check_Bottom")
        else :                                                          # Make Object go Up.
           self.int_oY -= self.int_oSpeed
           if(self.int_oY <= 0+self.int_border) :                       # If reached the top edge turn up.
              self.bool_oTurnUp = False
              print("Check_Top")
        #print("Object",self,"xPosition:", self.int_oX,self.bool_oTurnLeft,"yPosition:", self.int_oY,self.bool_oTurnUp) # Printing Object Number, Position on the X axis, Whether Object Going Left or not, Position on the Y axis, Whether Object Going Up or not.
    def checkCollision(self, other):
        if(self.int_oX + self.int_oWidth > other.int_oX and self.int_oX < other.int_oX + other.int_oWidth and self.int_oY + self.int_oHeight > other.int_oY and self.int_oY < other.int_oY + other.int_oHeight):
            self.bool_oTurnUp = not self.bool_oTurnUp
            ScoreBoard.int_score += 5
                    
    def checkCollision2(self, other): # Method for checking collision with other objects.
        if(self.int_oX + self.int_oWidth > other.int_oX and self.int_oX < other.int_oX + other.int_oWidth and self.int_oY + self.int_oHeight > other.int_oY and self.int_oY < other.int_oY + other.int_oHeight):
            if(self.int_oX + self.int_oWidth > other.int_oX and self.int_oX < other.int_oX + other.int_oWidth ):
                self.bool_oTurnLeft = not self.bool_oTurnLeft
            if(self.int_oY + self.int_oHeight > other.int_oY and self.int_oY < other.int_oY + other.int_oHeight):
                self.bool_oTurnUp = not self.bool_oTurnUp
            ScoreBoard.int_score = ScoreBoard.int_score + 10
    
    
    def drawShape(self) : # A method to draw Shapes
        fill(40,230,40) # Define color
        ellipse(self.int_oX,self.int_oY,self.int_oWidth,self.int_oHeight) # Draw a Rectangle
        
    def screenBorder(self): # Method for preventing going past the screen border.
        if(self.int_oX >= width-self.int_border-self.int_oWidth) :
            self.int_oX = width-self.int_border-self.int_oWidth
        if(self.int_oX <= self.int_border) :  
            self.int_oX = self.int_border
        if(self.int_oY >= height-self.int_border-self.int_oHeight) :
            self.int_oY = height-self.int_border-self.int_oHeight
        if(self.int_oY <= self.int_border) :  
            self.int_oY = self.int_border