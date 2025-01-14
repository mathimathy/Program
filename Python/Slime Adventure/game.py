from mod import keyboardHandler
import time
import map
from entity import player
from pynput import keyboard
from mod import vector
from mod.db import *
from mod import func
import vn
import battle
from entity import ennemy
from skills import basicAttack

class Game:
    def __init__(self):
        self.playing=True
        self.keyboard=keyboardHandler.Keyboard()
        self.needToRefresh=False
        self.gameMode="Battle"
        self.VN=""
        self.parties=[]
        self.ennemies=[]

    def setup(self):
        tileMap=conn.execute("SELECT * FROM TileMap").fetchall()
        self.map=map.Map(tileMap,(20,10))
        self.vn = vn.VN(self.keyboard)
        self.battle = battle.Battle(self.keyboard)
        self.player=player.Player(vector.Vector(5,5),conn.execute("SELECT * FROM Entity WHERE name LIKE 'player'").fetchall()[0],self.map,self.keyboard)
        self.parties.append(self.player)
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
    
    def playBattle(self):
        self.ennemies.append(ennemy.Ennemy(vector.none,[0,0,"E","WHITE","BRIGHT"],None,self.keyboard,"Squelette",{"hp":50,"mana":5,"ATK":10,"DEF":0},{"Attaque Basique":(basicAttack.Run,0)}))
        winning = self.battle.run(self.parties, self.ennemies)
        if winning:
            self.winBattle()
        else:
            self.lose()

    def update(self):
        if self.gameMode=="Map":
            self.playMap()
        elif self.gameMode=="VN":
            self.playVN()
        elif self.gameMode=="Battle":
            self.playBattle()
        

    def start(self):
        self.setup()
        while self.playing:
            self.update()
            time.sleep(0.08)
    
    def lose(self):
        func.clear()
        print("Vous avez perdu !")
        self.playing=False
    

    def winBattle(self):
        func.clear()
        print("Bravo !")
        time.sleep(2)
        self.gameMode="Map"
        self.needToRefresh=True