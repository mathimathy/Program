from pynput import keyboard as k
from mod import func
def Run(player,ennemies,keyboard):
    func.clear()
    prompt=""
    keyCode={}
    for index,ennemy in enumerate(ennemies):
        prompt+=f"{index}. {ennemy.name}"
        keyCode[k.KeyCode.from_char(str(index))]=index
    print(prompt)
    checking=True
    while checking:
        for key,index in keyCode.items():
            if keyboard.pressedKey==key:
                Attack(player,ennemies[index])
                checking=False

def Attack(player,entity):
    entity.dammage(player.stats["ATK"])