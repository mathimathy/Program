class Map:
    def __init__(self,map,dic,length,coll):
        self.playerMap=map
        self.oldTile=0
        self.dic = dic
        self.length=length
        self.coll=coll

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
                    drawableLine+=self.dic[el]
                except:
                    try:
                        drawableLine+=el.sprite
                    except:
                        drawableLine+=" "
            drawableMap+=drawableLine+"|\n"
        drawableMap+=BORDER
        print(drawableMap)
    
    def checkCollision(self, pos):
        return self.coll[self.playerMap[pos.y][pos.x]]