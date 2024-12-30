import colorama
from db import createColor
class Map:
    def __init__(self,map,tileMap,length):
        self.playerMap=map
        self.oldTile=0
        self.tileMap=tileMap
        self.length=length

    def setPlayer(self,player):
        self.playerMap[player.oldPos.y][player.oldPos.x]=self.oldTile
        self.oldTile=self.playerMap[player.pos.y][player.pos.x]
        self.playerMap[player.pos.y][player.pos.x]=player

    def draw(self):
        BORDER="*"+"-"*self.length[0]+"*"
        drawableMap=BORDER+"\n"
        for line in self.playerMap:
            drawableLine="|"
            for el in line:
                try:
                    drawableLine+=createColor(self.tileMap[el][1],self.tileMap[el][3],self.tileMap[el][4])
                except:
                    try:
                        drawableLine+=el.sprite
                    except:
                        drawableLine+=" "
            drawableMap+=drawableLine+"|\n"
        drawableMap+=BORDER
        print(drawableMap)
    
    def checkCollision(self, pos):
        return self.tileMap[self.playerMap[pos.y][pos.x]][2]