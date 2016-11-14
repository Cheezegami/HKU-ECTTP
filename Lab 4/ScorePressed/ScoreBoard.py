from Controls import Controls
from GenericObject import GenericObject
from ObjectRunner import ObjectRunner
class ScoreBoard():
    def __init__(self,int_score) : # Constructor
        self.int_score=int_score
        self.bool_mayClickMouse = True
        self.int_clickDelay = 20
        self.int_clickTimer = self.int_clickDelay
        
    def update(self):
        self.countScoreBoard()
        self.drawScoreBoard()
    
    def countScoreBoard(self):
        global objectList
        if(mousePressed):
            if(self.bool_mayClickMouse == True):
                self.bool_mayClickMouse = False
                self.int_clickDelay = self.int_clickTimer
                for i in range(0, len(ObjectRunner.objectList)):
                    if(mouseX < (ObjectRunner.objectList(i).int_oX)):
                         self.int_score += 20  
                           
                else:
                    self.int_score += 10
            
        if(self.bool_mayClickMouse == False):
            self.int_clickDelay -= 1
            print(self.int_clickDelay)
            if(self.int_clickDelay <= 0):
                self.bool_mayClickMouse = True
                
            
    def drawScoreBoard(self):
        textSize(30)
        text(self.int_score,width-200,50)