from mod.db import createColor,BASE_DIR
from mod.vector import *
import os
class Map:
    def __init__(self,tileMap,length):
        self.coord=Vector(0,0)
        self.playerMap=[]
        self.oldTile=0
        self.tileMap=tileMap
        self.length=length
        self.readMap()
    
    def readMap(self):
        filePath=os.path.join(BASE_DIR, f"data/map/{self.coord.x} {self.coord.y}.map")
        with open(filePath) as f:
            mapdata=f.read()
            mapdata=mapdata.split("\n")
            self.playerMap=[]
            for line in mapdata:
                column=line.split(",")
                intColumn=[]
                for el in column:
                    intColumn.append(int(el))
                self.playerMap.append(intColumn)
    
    def changeMap(self,dir):
        try:
            self.coord+=dir
            self.readMap()
            return True
        except:
            return False

    def setPlayer(self,player):
        if player.pos.x<0:
            if self.changeMap(left):
                player.pos.x=self.length[0]-1
        elif player.pos.x>=self.length[0]:
            if self.changeMap(right):
                player.pos.x=0
        elif player.pos.y<0:
            if self.changeMap(up):
                player.pos.y=self.length[1]-1
        elif player.pos.y>=self.length[1]:
            if self.changeMap(down):
                player.pos.y=0
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
        if pos.x<0:
            if self.changeMap(left):
                pos.x=self.length[0]-1
        elif pos.x>=self.length[0]:
            if self.changeMap(right):
                pos.x=0
        elif pos.y<0:
            if self.changeMap(up):
                pos.y=self.length[1]-1
        elif pos.y>=self.length[1]:
            if self.changeMap(down):
                pos.y=0
        return self.tileMap[self.playerMap[pos.y][pos.x]][2]