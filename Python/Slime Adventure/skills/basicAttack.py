from pynput import keyboard as k
from mod import func
import time
import random
def Run(player,ennemies,keyboard, isBot):
    if isBot:
        Attack(player, random.choice(ennemies))
    else:
        func.clear()
        prompt=""
        keyCode={}
        for index,ennemy in enumerate(ennemies):
            prompt+=f"{index}. {ennemy.name}"
            keyCode[k.KeyCode.from_char(str(index))]=index
        print(prompt)
        checking=True
        time.sleep(0.5)
        while checking:
            for key,index in keyCode.items():
                if keyboard.pressedKey==key:
                    func.clear()
                    if Attack(player,ennemies[index])==True:
                        print(f'{ennemies[index].name} est mort !')
                        del ennemies[index]
                    checking=False

def Attack(player,entity):
    return entity.dammage(player.stats["ATK"])