import keyboardHandler
import time
import map
import player
class Game:
    def __init__(self):
        self.playing=True
        self.keyboard=keyboardHandler.Keyboard()
        self.needToRefresh=False
        
    def setup(self):
        mapData=[
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        dic={0:" ",1:"█"}
        self.map=map.Map(mapData,dic,(15,10))
        self.player=player.Player(3,4,"o",self.map)
        self.draw()
    
    def draw(self):
        print("\n"*50)
        self.player.draw()
        self.map.draw()
        self.needToRefresh=False

    def update(self):
        if self.keyboard.pressedKey!=None:
            print(self.keyboard.pressedKey)
        if self.needToRefresh:
            self.draw()
        
    def start(self):
        self.setup()
        while self.playing:
            self.update()
            time.sleep(0.1)