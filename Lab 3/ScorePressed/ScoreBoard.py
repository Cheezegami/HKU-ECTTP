from Controls import Controls

class ScoreBoard():
    def __init__(self,int_score) : # Constructor
        self.int_score=int_score
        
    def update(self):
        self.countScoreBoard()
        self.drawScoreBoard()
    
    def countScoreBoard(self):
        if(mousePressed):
            self.int_score += 10
            
    def drawScoreBoard(self):
        textSize(30)
        text(self.int_score,width-200,50)