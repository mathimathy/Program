from pynput import keyboard
from mod import func
class Battle:
    def __init__(self, keyboard):
        self.parties=None
        self.enemies=None
        self.k=keyboard
    
    def playerTurn(self):
        func.clear()
        print("1. Attaquer\n2. Statistiques")
        while True:
            if self.k.pressedKey==keyboard.KeyCode.from_char("1"):
                self.parties[0].attack(self.ennemies)
                break

    def run(self, parties, ennemies):
        self.parties=parties
        self.ennemies=ennemies
        playing=True
        while playing:
            self.playerTurn()