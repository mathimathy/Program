from battle.lg import *
from classe import character
import random
import time
from battle import bot
from battle.displaystat import DisplayStat
class Battle:
    def __init__(self):
        self.monster = []
        self.territoire = character.current_territory[0]
        self.overvehicules = character.overvehicules_virt
        self.display_stat=DisplayStat()
    def create_monster(self):
        if self.territoire in character.territory:
            rand = random.randint(0,5)
            monster = character.monsters_surface[rand]
            for i in range(monster.nbre):
                self.monster.append(monster)
        elif self.territoire == "carthage":
            rand = random.randint(0,1)
            monster = character.monsters_carthage[rand]
            for i in range(monster.nbre):
                self.monster.append(monster)
        elif self.territoire == "replika":
            kollos_on = 0 #random.randint(0,1)
            if kollos_on:
                self.monster.append[character.special_monster["kollosus"]]
            else:
                rand = random.randint(0,5)
                monster = character.monsters_surface[rand]
                for i in range(monster.nbre):
                    self.monster.append(monster)
    def attack(self, lg, option, option_monster):
        monster = self.monster[option_monster-1]
        lg.attack_monster(monster, option)
        if monster.hp <= 0:
            del self.monster[option_monster-1]
    def choose_monster_to_attack(self, lg, option):
        print("\n"*50)
        j=1
        for m in self.monster:
            print(f"{j}: {m.name}\n")
            j+=1
        print('Choose an option')
        option_monster = input('> ')
        try:
            option_monster = int(option_monster)
        except:
            print("You need to type a number !")
            time.sleep(2.0)
            self.choose_monster_to_attack(lg, option)
        if option_monster <= j-1 and option_monster>0:
            self.attack(lg, option, option_monster)
        else:
            print("You need to choose on of the option")
            time.sleep(2.0)
            self.choose_monster_to_attack(lg, option)
    def choose_attack(self, lg):
        nbre_of_attack = len(lg.attack)
        print("\n"*50)
        print(lg.name +"\n")
        for j in range(nbre_of_attack):
            print(f"{j+1}: {lg.attack_name[j]}\n")
        print('Choose an option')
        option = input('>' )
        try:
            option = int(option)
            if option <= nbre_of_attack+1 and option>0:
                self.choose_monster_to_attack(lg, option)
            else:
                print("You need to choose one of the option")
                time.sleep(2.0)
                self.choose_attack(lg)
        except:
            print("You need to type a number !")
            time.sleep(2.0)
            self.choose_attack(lg)
        
    def turn(self):
        self.display_stat.display(character.virt_char,self.monster)
        for chr in character.virt_char:
            self.choose_attack(chr)
        for m in self.monster:
            ia = bot.Bot(m)
            ia.choose_attack()
        if len(self.monster)!=0 or len(character.virt_char)!=0:
            self.turn()
        elif len(self.monster)==0:
            return True
        elif len(character.virt_char)==0:
            return False