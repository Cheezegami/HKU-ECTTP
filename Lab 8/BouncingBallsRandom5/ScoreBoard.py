<<<<<<< HEAD
from Controls import Controls

class ScoreBoard():
    int_score = 0
    int_textSize = 28
    int_barWidth = int_textSize * 10
    int_marginTop = int_textSize / 2
    int_marginSide = int_marginTop
    int_barOffsetTop = int_textSize / 5
    int_barOffsetSide = int_barOffsetTop
    int_spacing = int_textSize / 5
    def __init__(self) : # Constructor
        self.bool_mayClickMouse = True
        self.int_clickDelay = 20
        self.int_clickTimer = self.int_clickDelay
        self.int_frameTimer = 0
        self.int_secondTimer = 0
        self.int_minuteTimer = 0
    def update(self):
        self.drawScoreBoard()
        
    def drawScoreBoard(self):
        self.int_frameTimer += 1
        if(self.int_frameTimer >= 60):
            self.int_secondTimer += 1
            self.int_frameTimer = 0
        if(self.int_secondTimer >=60):
            self.int_minuteTimer += 1
            self.int_secondTimer = 0
            
        for i in range(0, 2):
            int_boxHeight = self.int_marginTop+(self.int_textSize+self.int_spacing+self.int_barOffsetTop*2)*i
            fill(150,50,50,50)
            rect(width-self.int_barWidth-self.int_marginSide,int_boxHeight,self.int_barWidth,self.int_textSize + (self.int_barOffsetTop*2))
            fill(255)
            textSize(self.int_textSize)
            if(i == 0):
                text("Score:",width-self.int_barWidth-self.int_marginSide+self.int_barOffsetSide,int_boxHeight+self.int_textSize)
                fill(255,255,0)
                text(self.int_score,width-self.int_barWidth+(3*self.int_textSize)-self.int_marginSide+self.int_barOffsetSide,int_boxHeight+self.int_textSize)
            if(i == 1):
                text("Time:",width-self.int_barWidth-self.int_marginSide+self.int_barOffsetSide,int_boxHeight+self.int_textSize)
                fill(255,255,0)
                String_timerCounter = str(self.int_minuteTimer).zfill(2) + ":" + str(self.int_secondTimer).zfill(2) + ":" + str(self.int_frameTimer).zfill(2)
=======
from Controls import Controls

class ScoreBoard():
    int_score = 0
    int_textSize = 28
    int_barWidth = int_textSize * 10
    int_marginTop = int_textSize / 2
    int_marginSide = int_marginTop
    int_barOffsetTop = int_textSize / 5
    int_barOffsetSide = int_barOffsetTop
    int_spacing = int_textSize / 5
    def __init__(self) : # Constructor
        self.bool_mayClickMouse = True
        self.int_clickDelay = 20
        self.int_clickTimer = self.int_clickDelay
        self.int_frameTimer = 0
        self.int_secondTimer = 0
        self.int_minuteTimer = 0
    def update(self):
        self.drawScoreBoard()
        
    def drawScoreBoard(self):
        self.int_frameTimer += 1
        if(self.int_frameTimer >= 60):
            self.int_secondTimer += 1
            self.int_frameTimer = 0
        if(self.int_secondTimer >=60):
            self.int_minuteTimer += 1
            self.int_secondTimer = 0
            
        for i in range(0, 2):
            int_boxHeight = self.int_marginTop+(self.int_textSize+self.int_spacing+self.int_barOffsetTop*2)*i
            fill(150,50,50,50)
            rect(width-self.int_barWidth-self.int_marginSide,int_boxHeight,self.int_barWidth,self.int_textSize + (self.int_barOffsetTop*2))
            fill(255)
            textSize(self.int_textSize)
            if(i == 0):
                text("Score:",width-self.int_barWidth-self.int_marginSide+self.int_barOffsetSide,int_boxHeight+self.int_textSize)
                fill(255,255,0)
                text(self.int_score,width-self.int_barWidth+(3*self.int_textSize)-self.int_marginSide+self.int_barOffsetSide,int_boxHeight+self.int_textSize)
            if(i == 1):
                text("Time:",width-self.int_barWidth-self.int_marginSide+self.int_barOffsetSide,int_boxHeight+self.int_textSize)
                fill(255,255,0)
                String_timerCounter = str(self.int_minuteTimer).zfill(2) + ":" + str(self.int_secondTimer).zfill(2) + ":" + str(self.int_frameTimer).zfill(2)
>>>>>>> origin/master
                text(String_timerCounter,width-self.int_barWidth+(3*self.int_textSize)-self.int_marginSide+self.int_barOffsetSide,int_boxHeight+self.int_textSize)