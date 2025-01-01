from classe.command.command import Command
from classe import character
class Scan(Command):
    def __init__(self):
        super().__init__()
    def run(self, cmd):
        if self.isInit:
            if cmd[1] in character.chr:
                if cmd[1] in character.transf_char:
                    if cmd[1] in character.scan_char:
                        return "This character is already scanned"
                    else:
                        character.scan_char.append(cmd[1])
                        i=0
                        while i < len(character.transf_char):
                            if character.transf_char[i]==cmd[1]:
                                del character.transf_char[i]
                            i+=1
                        return "This character just be scanned"
                else:
                    return "This character isn't transfered"
            else:
                return "This character doesn't exist"
        else:
            return "The processus isn't started"
        