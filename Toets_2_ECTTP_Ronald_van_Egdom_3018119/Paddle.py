from Controls import Controls
class Paddle(object) :
    def __init__(self, int_oX,int_oY,int_oWidth,int_oHeight,int_oSpeed,int_border): #constructor
        self.int_oX = int_oX
        self.int_oY = int_oY
        self.int_oWidth = int_oWidth
        self.int_oHeight = int_oHeight
        self.int_oSpeed = int_oSpeed
        self.int_border = int_border

    def update(self):
        self.moveDirection()
        self.drawShape()
        self.screenBorder()
        
    def moveDirection(self) : # Method for moving the Objects.
        if(keyPressed) :
            if(key == Controls.String_controls[0] or key == Controls.String_altControls[0]):
                print("Pressed:",key)
                # Make Object go Right.
                self.int_oX += self.int_oSpeed
            elif(key == Controls.String_controls[1] or key == Controls.String_altControls[1]):
                print("Pressed:",key)
                # Make Object go Left.
                self.int_oX -= self.int_oSpeed
        #print("Object",self,"xPosition:", self.int_oX,self.bool_oTurnLeft,"yPosition:", self.int_oY,self.bool_oTurnUp) # Printing Object Number, Position on the X axis, Whether Object Going Left or not, Position on the Y axis, Whether Object Going Up or not.
        
    def drawShape(self) : # A method to draw Shapes
        fill(40,120,240) # Define color
        rect(self.int_oX,self.int_oY,self.int_oWidth,self.int_oHeight) # Draw a Rectangle
        
    def screenBorder(self): # Method for preventing going past the screen border.
        if(self.int_oX >= width-self.int_border-self.int_oWidth) :
            self.int_oX = width-self.int_border-self.int_oWidth
        if(self.int_oX <= self.int_border) :  
            self.int_oX = self.int_border
        if(self.int_oY >= height-self.int_border-self.int_oHeight) :
            self.int_oY = height-self.int_border-self.int_oHeight
        if(self.int_oY <= self.int_border) :  
            self.int_oY = self.int_border