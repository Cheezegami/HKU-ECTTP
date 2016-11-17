from Controls import Controls
from ScoreBoard import ScoreBoard

class GenericObject(object) :
    
    def __init__(self,int_oWidth,int_oHeight,int_oX,int_oY,int_oSpeed,String_form,int_movestyle,color_red,color_green,color_blue,int_border) : # Constructor
        self.int_oWidth = int_oWidth
        self.int_oHeight = int_oHeight
        self.int_oX = int_oX
        self.int_oY = int_oY
        self.int_oSpeed = int_oSpeed
        self.String_form = String_form
        self.int_movestyle = int_movestyle
        self.color_red = color_red
        self.color_green = color_green
        self.color_blue = color_blue
        self.int_border = int_border
        
        self.base_oWidth = int_oWidth
        self.base_oHeight = int_oHeight
        self.base_oX = int_oX
        self.base_oY = int_oY
        
        self.base_score = [0,0]
        self.next_score = [0,0]
        
        self.next_oWidth = int_oWidth
        self.next_oHeight = int_oHeight
        self.next_oX = int_oX
        self.next_oY = int_oY
        self.bool_oTurnLeft = False
        self.bool_oTurnUp = False
        self.bool_lerpPosition = False
        self.bool_lerpSize = False
        
        self.int_colorLow = 80
        self.int_colorMedium = 127
        self.int_colorHigh = 255
        
        self.int_spaceTimer = 60
        self.base_spaceTimer = self.int_spaceTimer
        self.bool_mayPressSpace = True
        self.float_sizeMultiplier = 2
        self.float_sizeRandomizer = self.float_sizeMultiplier
        self.float_lerpTime = [60.0,90.0]
        self.float_lerpStep = [0.0,0.0]
        self.canCheck = False;
        
        self.int_minWidth = int_oWidth / self.float_sizeRandomizer
        self.int_maxWidth = int_oWidth * self.float_sizeRandomizer 
        self.int_minHeight = int_oHeight / self.float_sizeRandomizer
        self.int_maxHeight = int_oHeight * self.float_sizeRandomizer
        
    @staticmethod
    def setupGenericObject() :
        ellipseMode(CORNER) # My calculations are based on the upper left corner of the ellipse.
    
    def update(self):
        self.printError()
        self.drawShape()
        self.checkMousePosition()
        self.alterObjectPosition()
        if self.int_movestyle == 0: # Auto Bouncing
            self.calculateDirection()
            self.changeSize()
            self.colorSelf()
        elif self.int_movestyle == 1: # Movable by Player
            self.moveDirection()
            self.changeSize()
            self.colorSelf()
            self.screenBorder()
        elif self.int_movestyle == 2: # Time Based Size
            self.calculateDirection()
            self.moveDirection()
            self.colorSelf()
            self.timeSize()
        else:
            print("not a valid movestyle specified for",self)
        #print(self.int_oWidth,self.int_oHeight,self.int_oX,self.int_oY,self.int_oSpeed,self.int_border,self.bool_oTurnLeft,self.bool_oTurnUp,"Test") # Debugging.

    def calculateDirection(self) : # Method for moving the Objects.
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

    def screenBorder(self):
        if(self.int_oX >= width-self.int_border-self.int_oWidth) :
            self.int_oX = width-self.int_border-self.int_oWidth
        if(self.int_oX <= self.int_border) :  
            self.int_oX = self.int_border
        if(self.int_oY >= height-self.int_border-self.int_oHeight) :
            self.int_oY = height-self.int_border-self.int_oHeight
        if(self.int_oY <= self.int_border) :  
            self.int_oY = self.int_border
        
    def checkCollision(self, other):
        if(self.int_oX > other.int_oX and self.int_oX < other.int_oX + other.int_oWidth):
            self.bool_oTurnLeft = not self.bool_oTurnLeft
            other.bool_oTurnLeft = not other.bool_oTurnLeft
            self.bool_oTurnUp = not self.bool_oTurnUp
            other.bool_oTurnUp =  not other.bool_oTurnUp
            
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
            if(key == Controls.String_controls[2] or key == Controls.String_altControls[2]):
                print("Pressed:",key)
                # Make Object go Down.
                self.int_oY += self.int_oSpeed     
            elif(key == Controls.String_controls[3] or key == Controls.String_altControls[3]):
                print("Pressed:",key)
                # Make Object go Up.              
                self.int_oY -= self.int_oSpeed
        #print("Object",self,"xPosition:", self.int_oX,self.bool_oTurnLeft,"yPosition:", self.int_oY,self.bool_oTurnUp) # Printing Object Number, Position on the X axis, Whether Object Going Left or not, Position on the Y axis, Whether Object Going Up or not.
        
    def colorSelf(self) : # A method to color an object based on its position on the screen.
        if (self.int_movestyle == 0): # If the assigned movestyle in the object creator is 0, the Auto Bouncing object.
            if(self.int_oWidth > self.base_oWidth * 2): 
                    # Very Subtle Yellow
                    self.color_red = self.int_colorMedium
                    self.color_green = self.int_colorMedium
                    self.color_blue = self.int_colorLow
            else:
                    # Very Suble Teal
                    self.color_red = self.int_colorLow
                    self.color_green = self.int_colorMedium
                    self.color_blue = self.int_colorMedium
        else:
          if self.int_oX < width/2 - self.int_oWidth/2: # Left side
            if self.int_oY < height/2 - self.int_oHeight/2: # Left top
                if(self.int_oWidth > self.base_oWidth * self.float_sizeMultiplier):
                    # Magenta
                    self.color_red = self.int_colorHigh
                    self.color_green = self.int_colorLow
                    self.color_blue = self.int_colorHigh
                else:
                    # Blue
                    self.color_red = self.int_colorLow
                    self.color_green = self.int_colorMedium
                    self.color_blue = self.int_colorHigh
            elif self.int_oY > height/2 - self.int_oHeight/2: # Left bottom
                if(self.int_oWidth > self.base_oWidth * self.float_sizeMultiplier):
                    # Red
                    self.color_red = self.int_colorHigh
                    self.color_green = self.int_colorLow
                    self.color_blue = self.int_colorLow
                else:
                    # Orange
                    self.color_red = self.int_colorHigh
                    self.color_green = self.int_colorMedium
                    self.color_blue = self.int_colorLow
          elif self.int_oX > width/2 - self.int_oWidth/2: # Right side
            if self.int_oY < height/2 - self.int_oHeight/2: # Right top
                if(self.int_oWidth > self.base_oWidth * self.float_sizeMultiplier):
                    # Cyan
                    self.color_red = self.int_colorLow
                    self.color_green = self.int_colorHigh
                    self.color_blue = self.int_colorHigh
                else:
                    #Green
                    self.color_red = self.int_colorLow
                    self.color_green = self.int_colorHigh
                    self.color_blue = self.int_colorLow
            elif self.int_oY > height/2 - self.int_oHeight/2: # Right Bottom
                if(self.int_oWidth > self.base_oWidth * self.float_sizeMultiplier):
                    #White
                    self.color_red = self.int_colorHigh
                    self.color_green = self.int_colorHigh
                    self.color_blue = self.int_colorHigh
                else:
                    #Yellow
                    self.color_red = self.int_colorHigh
                    self.color_green = self.int_colorHigh
                    self.color_blue = self.int_colorLow
    
    def timeSize(self) : #A method to alter the objects size based on time.
        self.int_oWidth = (height-self.base_oWidth)/60 * millis() %50000 / 150
        self.int_oHeight = (height-self.base_oWidth)/60 * millis() %50000 / 150
        
    def printError(self) : # A method to check errors.
        int_errorMargin = self.int_border + max(self.int_oWidth,self.int_oHeight) + 50 # Defining what's the minimal parameter required for an error message about the window size being to small to pop up.
        if(width <= int_errorMargin or height <= int_errorMargin) : # Giving an error when the window is too small for the objects to move on.
           print("The window size is too small, make sure both the width:(", width ,") and the height:(", height ,") of the window are bigger than ", int_errorMargin ,"for the optimal screen traversing experience!") # Printing the error to the console.
           
    def drawShape(self) : # A method to draw Shapes
        fill(self.color_red,self.color_green,self.color_blue) # Define color
        if(self.String_form == "ellipse") : # If an ellipse draw an ellipse.
            ellipse(self.int_oX,self.int_oY,self.int_oWidth,self.int_oHeight) # Draw an Ellipse
        elif(self.String_form == "rectangle") : # If a rectangle draw a rectangle.
            rect(self.int_oX,self.int_oY,self.int_oWidth,self.int_oHeight) # Draw a Rectangle
        else : # If no shape or having a invalid shape.
            print(self, "is missing a shape or having an invalid shape.")

    def changeSize(self):
        if(keyPressed) : # If any key is pressed.
            if((key == Controls.String_controls[4] or key == Controls.String_altControls[4]) and self.bool_lerpSize == False and self.bool_mayPressSpace == True): # Gets the fourth key out of both arrays within the Controls class.
                print("Pressed:",key)
                self.base_score[1] = ScoreBoard.int_score
                self.next_score[1] = 25 + self.base_score[1]
                self.float_lerpStep[1] = 0.0
                self.base_oWidth = self.int_oWidth
                self.base_oHeight = self.int_oHeight
                self.next_oWidth = self.base_oWidth * self.float_sizeMultiplier
                self.next_oHeight = self.base_oHeight * self.float_sizeMultiplier
                self.bool_mayPressSpace = False
                self.bool_lerpSize = True
                self.int_spaceTimer = 0
        if(self.bool_mayPressSpace == False):
            self.int_spaceTimer += 1
            if(self.int_spaceTimer >= self.float_lerpTime[1]*1.5):
                if(self.bool_lerpSize == False):
                    self.base_score[1] = ScoreBoard.int_score
                    self.next_score[1] = 25 + self.base_score[1]
                    self.base_oWidth = self.int_oWidth
                    self.base_oHeight = self.int_oHeight
                    self.next_oWidth = self.base_oWidth / self.float_sizeMultiplier
                    self.next_oHeight = self.base_oHeight / self.float_sizeMultiplier
                    self.bool_lerpSize = True
                    self.float_lerpStep[1] = 0.0
                if(self.int_spaceTimer >= self.float_lerpTime[1]):
                    self.bool_mayPressSpace = True
                    self.int_spaceTimer = 0

    def checkMousePosition(self):
        if(mousePressed == True):
            if(mouseX >= self.int_oX and mouseX <= self.int_oX + self.int_oWidth and mouseY >= self.int_oY and mouseY <= self.int_oY + self.int_oHeight and self.bool_lerpPosition == False):
                self.base_score[0] = ScoreBoard.int_score
                self.next_score[0] = self.base_score[0] + 20
                self.float_lerpStep[0] = 0.0
                self.base_oX = self.int_oX
                self.base_oY = self.int_oY
                self.next_oX = random(width-self.int_border-self.int_oWidth)
                self.next_oY = random(height-self.int_border-self.int_oHeight)
                self.base_oWidth = self.int_oWidth
                self.base_oHeight = self.int_oHeight
                self.next_oWidth = random(self.int_minWidth,self.int_maxWidth)
                if(self.base_oWidth == self.base_oHeight):
                    self.next_oHeight = self.next_oWidth
                else:
                    self.next_oHeight = random(self.int_minWidth,self.int_maxWidth)
                self.bool_lerpPosition = True
                

    def alterObjectPosition(self):
        if(self.bool_lerpPosition == True):
            self.float_lerpStep[0] += 1/self.float_lerpTime[0]
            ScoreBoard.int_score = ceil(lerp(self.base_score[0],self.next_score[0],self.float_lerpStep[0]))
            self.int_oX = lerp(self.base_oX,self.next_oX,self.float_lerpStep[0])
            self.int_oY = lerp(self.base_oY,self.next_oY,self.float_lerpStep[0])
            self.int_oWidth = lerp(self.base_oWidth,self.next_oWidth,self.float_lerpStep[0])
            self.int_oHeight = lerp(self.base_oHeight,self.next_oHeight,self.float_lerpStep[0])
            if(self.float_lerpStep[0] >= 1.0):
                self.bool_lerpPosition = False
                self.float_lerpStep[0] = 0.0
        if(self.bool_lerpSize == True):
            self.float_lerpStep[1] += 1/self.float_lerpTime[1]
            ScoreBoard.int_score = ceil(lerp(self.base_score[1],self.next_score[1],self.float_lerpStep[1]))
            self.int_oWidth = lerp(self.base_oWidth,self.next_oWidth,self.float_lerpStep[1])
            self.int_oHeight = lerp(self.base_oHeight,self.next_oHeight,self.float_lerpStep[1])
            if(self.float_lerpStep[1] >= 1.0):
                self.bool_lerpSize = False
                self.float_lerpStep[1] = 0.0
        
            