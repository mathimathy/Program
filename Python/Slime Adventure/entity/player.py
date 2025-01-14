from entity.entity import Entity
from pynput import keyboard
from skills import basicAttack
from mod import func
import colorama
import time
class Player(Entity):
    def __init__(self,pos,sprite,map,keyboard):
        super().__init__(pos,sprite,map,keyboard)
        self.skills={"Attaque Basique": (basicAttack.Run,0)}
        self.name=colorama.Fore.BLUE+"Player"+colorama.Fore.RESET
        self.stats={
            "hp":200,
            "mana":100,
            "ATK":5,
            "DEF":2
        }
    
    def dammage(self, dmg):
        if dmg>self.stats["DEF"]:
            self.stats["hp"]-=(dmg-self.stats["DEF"])
        if self.stats["hp"]<=0:
            return True
    
    def activateSkill(self, skill, ennemies):
        if self.stats["mana"]>=self.skills[skill][1]:
            self.stats["mana"]-=self.skills[skill][1]
            self.skills[skill][0](self,ennemies,self.k, False)
            return True
        else:
            return False
    
    def learnSkill(self, name, function):
        self.skills[name]=function
    
    def attack(self,ennemies):
        func.clear()
        prompt=""
        keyCode={}
        for index,name in enumerate(self.skills.keys()):
            prompt+=f"{index}. {name}"
            keyCode[keyboard.KeyCode.from_char(str(index))]=index
        print(prompt)
        checking=True
        time.sleep(0.5)
        while checking:
            for key,index in keyCode.items():
                if self.k.pressedKey==key:
                    if self.activateSkill(list(self.skills.keys())[index], ennemies):
                       checking=False
                    else:
                        print("Vous n'avez pas assez de mana !")