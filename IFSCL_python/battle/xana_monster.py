#Surface monster
class monster:
    def __init__(self):
        pass
    def dammage(self, amount):
        self.hp-=amount
    def attack_lg(self, who, attack_id):
        if self.attack[attack_id]:
            who.devirt()
        else:
            who.dammage(self.attack[attack_id])

class Kankrelat(monster):
    def __init__(self):
        super().__init__()
        self.name="Kankrelat"
        self.hp = 25
        self.attack=[10]
        self.attack_name=["Laser"]
        self.nbre=5
    
class Hornet(monster):
    def __init__(self):
        super().__init__()
        self.name="Hornet"
        self.hp=50
        self.attack=[20,5,40]
        self.attack_name=["Laser", "Poison", "Tackle"]
        self.nbre=5

class Blok(monster):
    def __init__(self):
        super().__init__()
        self.name="Blok"
        self.hp=50
        self.attack=[15,10,25,True]
        self.attack_name=["Laser", "Freeze Spray", "Fire Rings", "Blok Wall"]
        self.nbre=4

class Krab(monster):
    def __init__(self):
        super().__init__()
        self.name="Krab"
        self.hp=95
        self.attack=[10,40,True,True]
        self.attack_name=["Laser", "Charged Laser", "Pulse Beam", "Impale with leg"]
        self.nbre=2

class Megatank(monster):
    def __init__(self):
        super().__init__()
        self.name="Megatank"
        self.hp=100
        self.attack=[50,100]
        self.attack_name=["Circular Laser", "Flattening"]
        self.nbre=1

class Tarantula(monster):
    def __init__(self):
        super().__init__()
        self.name="Tarantula"
        self.hp=125
        self.attack=[20]
        self.attack_name=["Laser"]
        self.nbre=2

#Carthage monster
class Creeper(monster):
    def __init__(self):
        super().__init__()
        self.name="Creeper"
        self.hp=20
        self.attack=[40]
        self.attack_name=["Laser"]
        self.nbre=5

class Manta(monster):
    def __init__(self):
        super().__init__()
        self.name="Manta"
        self.hp=75
        self.attack=[40,100]
        self.attack_name=["Laser", "Mines"]
        self.nbre=3