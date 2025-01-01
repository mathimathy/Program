from tkinter import Toplevel
import classe.character as character
from classe.command.command import Command
class Transf(Command):
    def __init__(self):
        super().__init__()
    def run(self, cmd):
        if self.isInit:
            if cmd[1] in character.chr:
                for chr in character.virt_char:
                    if chr.name == cmd[1]:
                        return "This character is already virtualized"
                if cmd[1] in character.transf_char or cmd[1] in character.scan_char:
                    return "This character is already transfered"
                elif len(character.transf_char)==3:
                    return "You cannot transfer more than three lyokowarrior at the same time"
                else:
                    character.transf_char.append(cmd[1])
                    return "This character just be transfered"
            else:
                return "This character doesn't exist"
        else:
            return "The processus isn't started"