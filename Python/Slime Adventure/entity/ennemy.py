from entity.entity import Entity
from pynput import keyboard
from skills import basicAttack
class Ennemy(Entity):
    def __init__(self,pos,sprite,map,keyboard, name, stats, skills):
        super().__init__(pos,sprite,map,keyboard)
        self.name=name
        self.skills=skills
        self.stats=stats
    
    def dammage(self, dmg):
        self.stats["hp"]-=(dmg-self.stats["DEF"])
        if self.stats["hp"]<=0:
            return True
    
    def activateSkill(self, skill, ennemies):
        self.skills[skill](self,ennemies,self.k)
    
    def attack(self,ennemies):
        prompt=""
        keyCode={}
        for index,name in enumerate(self.skills.keys()):
            prompt+=f"{index}. {name}"
            keyCode[keyboard.KeyCode.from_char(str(index))]=index
        print(prompt)
        while True:
           for key,index in keyCode.items():
               if self.k.pressedKey==key:
                   self.activateSkill(list(self.skills.keys())[index], ennemies)
                   break