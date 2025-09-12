import colorama
from pynput import keyboard
class Character:
    def __init__(self, name, color, style, keyboard):
        self.name=name
        self.color=color
        self.style=style
        self.k=keyboard
    
    def __str__(self):
        return self.color+self.style+self.name+colorama.Style.RESET_ALL

    def __format__(self, format):
        return str(self)

    def say(self, msg, wait=True):
        print(f"{self}: {msg}")
        if wait:
            while self.k.pressedKey!=keyboard.Key.enter:
                pass
    
    def choice(self, msg, choices):
        self.say(msg, False)
        print(f"1. {choices[0][0]}\n2. {choices[1][0]}")
        while True:
            
            if self.k.pressedKey==keyboard.KeyCode.from_char('1') or self.k.pressedKey==keyboard.KeyCode.from_char('&'):
                print(1)
                return choices[0][1]
            elif self.k.pressedKey==keyboard.KeyCode.from_char('2') or self.k.pressedKey==keyboard.KeyCode.from_char('é'):
                print(2)
                return choices[1][1]