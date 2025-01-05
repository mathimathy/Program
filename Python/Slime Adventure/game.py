from mod import keyboardHandler
import time
import map
from entity import player
from pynput import keyboard
from mod import vector
from mod.db import *
from mod import func
import vn

class Game:
    def __init__(self):
        self.playing=True
        self.keyboard=keyboardHandler.Keyboard()
        self.needToRefresh=False
        self.gameMode="Map"
        self.VN=""

    def setup(self):
        tileMap=conn.execute("SELECT * FROM TileMap").fetchall()
        self.map=map.Map(tileMap,(20,10))
        self.vn = vn.VN(self.keyboard)
        self.player=player.Player(vector.Vector(5,5),conn.execute("SELECT * FROM Entity WHERE name LIKE 'player'").fetchall()[0],self.map)
        self.draw()

    def draw(self):
        func.clear()
        self.player.draw()
        self.map.draw()
        self.needToRefresh=False
    
    def playMap(self):
        match self.keyboard.pressedKey:
            case keyboard.Key.up:
                self.player.move(vector.up)
                self.needToRefresh=True
            case keyboard.Key.down:
                self.player.move(vector.down)
                self.needToRefresh=True
            case keyboard.Key.left:
                self.player.move(vector.left)
                self.needToRefresh=True
            case keyboard.Key.right:
                self.player.move(vector.right)
                self.needToRefresh=True
            case _:
                pass


        if self.needToRefresh:
            self.draw()
        
    def playVN(self):
        self.VN="debug"
        self.vn.run(self.VN)

    def update(self):
        if self.gameMode=="Map":
            self.playMap()
        elif self.gameMode=="VN":
            self.playVN()
        

    def start(self):
        self.setup()
        while self.playing:
            self.update()
            time.sleep(0.08)