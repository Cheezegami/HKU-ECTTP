class Block(object) :
    def __init__(self, int_oX,int_oY,int_oWidth,int_oHeight):
        self.int_oWidth = int_oWidth
        self.int_oHeight = int_oHeight
        self.int_oX = int_oX
        self.int_oY = int_oY
        
    def update(self):
        self.drawShape()

    def drawShape(self) : # A method to draw Shapes
        fill(240, 40, 40) # Define color
        rect(self.int_oX,self.int_oY,self.int_oWidth,self.int_oHeight) # Draw a Rectangle