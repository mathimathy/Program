class Player:
    def __init__(self,x,y,sprite,map):
        self.pos=(x,y)
        self.sprite=sprite
        self.map=map
    
    def draw(self):
        self.map.setPlayer(self)