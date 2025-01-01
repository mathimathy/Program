from classe.command.command import Command
from classe import character
from battle import lg
class Overvehicule(Command):
    def __init__(self):
        super().__init__()
    def run(self, cmd):
        if self.isInit:
            try:
                if cmd[2] == "demater":
                    if cmd[1] in character.overvehicules:
                        for over in character.overvehicules_virt:
                            if over.name == cmd[1]:
                                over.devirt()
                                return "The overvehicule is devirtualized"
                    else:
                        return "This overvehicule doesn't exist"
            except:
                if cmd[1] in character.overvehicules:
                    if lg.Overvehicule(cmd[1]) in character.overvehicules_virt:
                        return "This overvehicule is already virtualized"
                    else:
                        character.overvehicules_virt.append(lg.Overvehicule(cmd[1]))
                        return "The overvehicule is virtualized"
                else:
                    return "This subcommand doesn't exist"
        else:
            return "The processus isn't started"