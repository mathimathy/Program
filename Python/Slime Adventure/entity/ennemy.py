from entity.entity import Entity
from pynput import keyboard
from skills import basicAttack
import random
class Ennemy(Entity):
    def __init__(self,pos,sprite,map,keyboard, name, stats, skills):
        super().__init__(pos,sprite,map,keyboard)
        self.name=name
        self.skills=skills
        self.stats=stats
    
    def dammage(self, dmg):
        if dmg>self.stats["DEF"]:
            self.stats["hp"]-=(dmg-self.stats["DEF"])
        if self.stats["hp"]<=0:
            return True
    
    def activateSkill(self, skill, ennemies):
        if self.stats["mana"]>=self.skills[skill][1]:
            self.stats["mana"]-=self.skills[skill][1]
            self.skills[skill][0](self,ennemies,self.k, True)
            return True
        else:
            return False
    
    def attack(self,ennemies):
        weights=[0.99 if skill[1]==0 else 1/skill[1] for skill in self.skills.values()]
        possibleSkills = random.choices(list(self.skills.keys()), weights=weights)
        self.activateSkill(random.choice(possibleSkills), ennemies)