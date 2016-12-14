# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Toets 2.
# My laptop crashed halfway through the excercise, this severely reduced the features of the code. ;^(

from Ball import Ball
from Paddle import Paddle
from Block import Block
from ScoreBoard import ScoreBoard

#Arrays to store objects.
paddleList = [] # Array in which the paddles are contained.
ballList = [] # Array in which the balls are contained.
blockList = [] # Array in which the blocks are contained.

#Making variables.
int_blockLength = 180
int_blockHeight = 80

score = ScoreBoard()
int_border = 0 # Minimum object distance from edge of the screen.
int_bgColor = 50 # Background color.
def setup(): # Defining parameters that run once.
    size(1400,800) # Screen size. (Width,Height)
    # Object Creation.
    ellipseMode(CORNER)
    paddleList.append(Paddle(width/2-100,height-50,200,50,6,int_border)) # First Paddle.
    ballList.append(Ball(width/2,height/2,100,100,5,int_border)) # First Ball.
    blockList.append(Block(width/2 - int_blockLength / 2, 100, int_blockLength, int_blockHeight)) # First Block
    blockList.append(Block(width/2 - int_blockLength / 2 - 200, 100, int_blockLength, int_blockHeight)) # Second Block
    blockList.append(Block(width/2 - int_blockLength / 2 + 200, 100, int_blockLength, int_blockHeight)) # Third Block
    blockList.append(Block(width/2 - int_blockLength / 2 - 300, 200, int_blockLength, int_blockHeight)) # Fourth Block
    blockList.append(Block(width/2 - int_blockLength / 2 + 300, 200, int_blockLength, int_blockHeight)) # Fifth Block

def draw(): # Continually runs as long as the program runs.
    background(int_bgColor) # Cleaning the screen from previous draws.
    for i in range(0, len(ballList)) : # For loop based on total number of objects
        Ball.update(ballList[i]) # Run the methods in the GenericObject class responsible for defining the position and drawing the objects.
        for j in range(0, len(blockList)):
            Block.update(blockList[j])
            ballList[i].checkCollision2(blockList[j])
        for k in range(0, len(paddleList)):
            Paddle.update(paddleList[k])
            ballList[i].checkCollision(paddleList[k])
    ScoreBoard.update(score)