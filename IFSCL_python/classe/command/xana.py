from tkinter import Label
from classe import character
import time
import random
from classe.command.command import Command
class Xana(Command):
    def __init__(self):
        super().__init__()
    def attack(self):
        i=0
        attacktype = 0 #random.randint(0,2)
        if attacktype == 0:
            character.xana_tour.clear()
            character.xana_tour.append(random.randint(1,10))
            character.xana_territory.clear()
            territory = random.randint(0,3)
            if territory==0:
                character.xana_territory.append("mountain")
            elif territory==1:
                character.xana_territory.append("ice")
            elif territory==2:
                character.xana_territory.append("desert")
            elif territory==3:
                character.xana_territory.append("forest")

    def run(self, cmd):
        if self.isInit:
            if cmd[1] == "exe":
                self.attack()
                return "An attack is started !"
            else:
                return "This subcommand doesn't exist"
        else:
            "This processus isn't started"