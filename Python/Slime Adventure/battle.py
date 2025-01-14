from pynput import keyboard
from mod import func
class Battle:
    def __init__(self, keyboard):
        self.parties=None
        self.enemies=None
        self.k=keyboard
    
    def playerTurn(self, party):
        print("1. Attaquer\n2. Statistiques")
        while True:
            if self.k.pressedKey==keyboard.KeyCode.from_char("1"):
                party.attack(self.ennemies)
                break
            elif self.k.pressedKey==keyboard.KeyCode.from_char("2"):
                func.clear()
                stats="\bPARTY\n-------------\n"
                for party in self.parties:
                    hp=party.stats["hp"]
                    mana=party.stats["mana"]
                    ATK=party.stats["ATK"]
                    DEF=party.stats["DEF"]
                    stats+=f"{party.name}:\nhp: {hp}\nmana: {mana}\nATK: {ATK}\nDEF: {DEF}\n"
                stats+="-------------\n\nENNEMY\n-------------\n"
                for ennemy in self.ennemies:
                    hp=ennemy.stats["hp"]
                    mana=ennemy.stats["mana"]
                    ATK=ennemy.stats["ATK"]
                    DEF=ennemy.stats["DEF"]
                    stats+=f"{ennemy.name}:\nhp: {hp}\nmana: {mana}\nATK: {ATK}\nDEF: {DEF}\n"
                stats+="-------------\n"
                print(stats)
                print("1. Attaquer\n2. Statistiques")
    
    def ennemyTurn(self, ennemy):
        ennemy.attack(self.parties)

    def run(self, parties, ennemies):
        self.parties=parties
        self.ennemies=ennemies
        func.clear()
        playing=True
        while playing:
            for party in self.parties:
                self.playerTurn(party)
            
            for ennemy in self.ennemies:
                self.ennemyTurn(ennemy)

            if len(self.ennemies)==0:
                playing=False
                return True
            elif len(self.parties)==0:
                playing=False
                return False