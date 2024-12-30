class Map:
    def __init__(self,map,dic,length):
        self.map=map
        self.playerMap=map
        self.dic = dic
        self.length=length

    def setPlayer(self,player):
        self.resetPlayerMap()
        self.playerMap[player.pos[0]][player.pos[1]]=player

    def draw(self):
        BORDER="*"+"-"*self.length[0]+"*"
        drawableMap=BORDER+"\n"
        for line in self.map:
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
    
    def resetPlayerMap(self):
        self.playerMap=self.map