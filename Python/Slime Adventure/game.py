import mod.keyboardHandler as keyboardHandler
import time
import map
import entity.player as player
from pynput import keyboard
import mod.vector as vector
from mod.db import *

class Game:
    def __init__(self):
        self.playing=True
        self.keyboard=keyboardHandler.Keyboard()
        self.needToRefresh=False
        
    def setup(self):
        tileMap=conn.execute("SELECT * FROM TileMap").fetchall()
        self.map=map.Map(tileMap,(20,10))
        self.player=player.Player(vector.Vector(5,5),conn.execute("SELECT * FROM Entity WHERE name LIKE 'player'").fetchall()[0],self.map)
        self.draw()
    
    def draw(self):
        print("\n"*50)
        self.player.draw()
        self.map.draw()
        self.needToRefresh=False

    def update(self):
        if self.keyboard.pressedKey==keyboard.Key.up:
            self.player.move(vector.up)
            self.needToRefresh=True
        elif self.keyboard.pressedKey==keyboard.Key.down:
            self.player.move(vector.down)
            self.needToRefresh=True
        elif self.keyboard.pressedKey==keyboard.Key.right:
            self.player.move(vector.right)
            self.needToRefresh=True
        elif self.keyboard.pressedKey==keyboard.Key.left:
            self.player.move(vector.left)
            self.needToRefresh=True

        if self.needToRefresh:
            self.draw()
        
    def start(self):
        self.setup()
        while self.playing:
            self.update()
            time.sleep(0.08)