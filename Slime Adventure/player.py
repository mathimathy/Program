from db import createColor
class Player:
    def __init__(self,pos,sprite,map):
        self.pos=pos
        self.oldPos=self.pos.copy()
        self.sprite=createColor(sprite[2],sprite[3],sprite[4])
        self.map=map
        self.speed=1
    
    def draw(self):
        self.map.setPlayer(self)
    
    def move(self, dir):
        self.oldPos=self.pos.copy()
        pos=self.pos.copy()+dir*self.speed
        if not self.map.checkCollision(pos):
            self.pos=pos.copy()
        else:
            self.pos=self.oldPos.copy()