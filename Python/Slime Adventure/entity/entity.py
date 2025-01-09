from mod.db import createColor
class Entity:
    def __init__(self,pos,sprite,map,keyboard):
        self.pos=pos
        self.oldPos=self.pos.copy()
        self.sprite=createColor(sprite[2],sprite[3],sprite[4])
        self.map=map
        self.speed=1
        self.k=keyboard

    def draw(self):
        self.map.setEntity(self)

    def move(self, dir):
        self.oldPos=self.pos.copy()
        pos=self.pos.copy()+dir*self.speed
        if not self.map.checkCollision(pos):
            self.pos=pos.copy()
        else:
            self.pos=self.oldPos.copy()