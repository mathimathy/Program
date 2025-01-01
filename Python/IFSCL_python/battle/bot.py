from classe import character
import random
class Bot:
    def __init__(self, monster):
        self.monster = monster
    def attack(self, option, option_lg, islw):
        if islw:
            lg = character.virt_char[option_lg-1]
            self.monster.attack_lg(lg, option)
            if lg.hp <= 0:
                lg.devirt()
        else:
            overvehicule = character.overvehicules_virt[option_lg-4]
            self.monster.attack_lg(overvehicule, option)
            if overvehicule.hp <= 0:
                overvehicule.devirt()
    def choose_lg_to_attack(self, option):
        if len(character.overvehicules_virt)!=0:
            islw = random.randint(0,1)
        else:
            islw=1
        if islw:
            if len(character.virt_char)==1:
                self.attack(option, 0, islw)
            elif len(character.virt_char)==0:
                character.value["isOn"]=False
                exit("Xana Win")
            else:
                option_lg = random.randint(0,len(character.virt_char)-1)
                self.attack(option, option_lg, islw)
        else:
            if len(character.overvehicules_virt)==1:
                self.attack(option, 0, islw)
            else:
                option_overvehicule = random.randint(0,len(character.overvehicules_virt)-1)
                self.attack(option, option_overvehicule, islw)
    def choose_attack(self):
        nbre_of_attack = len(self.monster.attack)
        option = random.randint(0,nbre_of_attack-1)
        self.choose_lg_to_attack(option)