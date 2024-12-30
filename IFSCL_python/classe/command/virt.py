from classe.command.command import Command
from classe import character
from battle import lg
class Virt(Command):
    def __init__(self):
        super().__init__()
    def run(self, cmd):
        if self.isInit:
            if cmd[1]=="to":
                if cmd[2]=="carthage":
                    character.current_territory[0] = "carthage"
                    return "The position is registred"
                elif cmd[2] in character.territory:
                    try:
                        if int(cmd[3]) > 0 and int(cmd[3]) < 10:
                            character.current_territory[0] = cmd[2]
                            character.position.append(int(cmd[3]))
                            return "The position is registered"
                    except:
                        return "You need to type a tower number (from 1 to 10)"
            elif cmd[1]=="exe":
                for chr in character.scan_char:
                    if chr == "odd":
                        character.virt_char.append(lg.Odd())
                    if chr == "yumi":
                        character.virt_char.append(lg.Yumi())
                    if chr == "ulrich":
                        character.virt_char.append(lg.Ulrich())
                    if chr == "aelita":
                        character.virt_char.append(lg.Aelita())
                character.scan_char.clear()
                return "The LyokoWarrior is virtualized"
            else:
                return "this subcommand doesn't exist"
        else:
            return "The processus isn't started"