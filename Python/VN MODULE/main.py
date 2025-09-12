from character import Character
import colorama
from keyboardHandler import Keyboard

k = Keyboard()
e = Character("emily", colorama.Fore.WHITE, colorama.Style.BRIGHT, k)
n = Character("nathan", colorama.Fore.BLUE, colorama.Style.BRIGHT, k)

e.say("Salut")
def yes():
    n.say("Cool !")

def no():
    n.say("Dommage...")
    
n.choice("Comment vas-tu ?", [
    ["Ca va", yes],
    ["Boff...", no]
])()