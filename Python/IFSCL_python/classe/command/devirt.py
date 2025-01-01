from classe.command.command import Command
from classe import character
class Devirt(Command):
    def __init__(self):
        super().__init__()
    def run(self, cmd):
        if self.isInit:
            virt_name=[]
            for chr in character.virt_char:
                virt_name.append(chr.name)
            if cmd[1] in virt_name:
                for chara in character.virt_char:
                    if cmd[1] == chara.name:
                        chara.devirt()
                        return "The lyokowarrior is devirtualized sucessfully"
            else:
                return "This character isn't virtualized"
        else:
            return "The processus isn't started"