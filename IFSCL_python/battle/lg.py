from classe.character import virt_char, overvehicules_virt
#LyokoWarrior
class LyokoWarrior:
    def __init__(self, lg):
        self.name=lg
        self.hp=100
        self.mana=10
    def dammage(self, amount):
        self.hp-=amount
    def attack_monster(self, who, attack_id):
        if self.mana-self.attack_cost[attack_id-1] < 0:
            attack_id=0
        else:
            who.dammage(self.attack[attack_id-1])
            self.mana-=self.attack_cost[attack_id-1]
    def devirt(self):
        j=1
        for char in virt_char:
            if char.name==self.name:
                k=j
            j+=1
        del virt_char[k-1]

class Odd(LyokoWarrior):
    def __init__(self):
        super().__init__("odd")
        self.attack=[10]
        self.attack_name=["Flèche Laser"]
        self.attack_cost=[0]

class Yumi(LyokoWarrior):
    def __init__(self):
        super().__init__("yumi")
        self.attack=[10]
        self.attack_name=["Eventail"]
        self.attack_cost=[0]

class Ulrich(LyokoWarrior):
    def __init__(self):
        super().__init__("ulrich")
        self.attack=[10]
        self.attack_name=["Impact"]
        self.attack_cost=[0]

class Aelita(LyokoWarrior):
    def __init__(self):
        super().__init__("aelita")
        self.attack=[20]
        self.attack_name=["Matérialisation"]
        self.attack_cost=[2]

#Overvehicules
class Overvehicule:
    def __init__(self, overvehicules):
        self.name=overvehicules
        self.hp=100
    def dammage(self, amount):
        self.hp-=amount
    def devirt(self):
        del overvehicules_virt[self.name]