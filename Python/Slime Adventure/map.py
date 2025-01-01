from mod.db import createColor,BASE_DIR
from mod.vector import *
import os
class Map:
    def __init__(self,tileMap,length):
        self.coord=Vector(0,0)
        self.map=[]
        self.oldTile=0
        self.tileMap=tileMap
        self.length=length
        self.readMap()
    
    def readMap(self):
        filePath=os.path.join(BASE_DIR, f"data/map/{self.coord.x} {self.coord.y}.map")
        with open(filePath) as f:
            mapdata=f.read()
            mapdata=mapdata.split("\n")
            self.map=[]
            for line in mapdata:
                column=line.split(",")
                intColumn=[]
                for el in column:
                    intColumn.append(int(el))
                self.map.append(intColumn)
    
    def changeMap(self,dir):
        try:
            self.coord+=dir
            self.readMap()
            return True
        except:
            return False

    def setEntity(self,entity):
        if entity.pos.x<0:
            if self.changeMap(left):
                entity.pos.x=self.length[0]-1
        elif entity.pos.x>=self.length[0]:
            if self.changeMap(right):
                entity.pos.x=0
        elif entity.pos.y<0:
            if self.changeMap(up):
                entity.pos.y=self.length[1]-1
        elif entity.pos.y>=self.length[1]:
            if self.changeMap(down):
                entity.pos.y=0
        self.map[entity.oldPos.y][entity.oldPos.x]=self.oldTile
        self.oldTile=self.map[entity.pos.y][entity.pos.x]
        self.map[entity.pos.y][entity.pos.x]=entity

    def draw(self):
        BORDER="*"+"-"*self.length[0]+"*"
        drawableMap=BORDER+"\n"
        for line in self.map:
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
        return self.tileMap[self.map[pos.y][pos.x]][2]