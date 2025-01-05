from vnScript import debug
from mod.character import Character
import colorama
class VN:
    def __init__(self, keyboard):
        self.chars={"emily": Character("Emily", colorama.Fore.BLUE, colorama.Style.BRIGHT, keyboard)}
        self.scripts={"debug": debug.Run}
    
    def run(self, script):
        self.scripts[script](self.chars)