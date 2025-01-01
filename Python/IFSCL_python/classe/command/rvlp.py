from classe import character
from classe.command.command import Command
import time
class Rvlp(Command):
    def __init__(self):
        super().__init__()
    def run(self, cmd):
        try:
            cmd[1]=int(cmd[1])
            self.time = cmd[1]
            return "Time added"
        except:
            if cmd[1]=="exe":
                time.sleep(self.time)
                for lg in character.virt_char:
                    lg.devirt()
                for over in character.overvehicules_virt:
                    over.devirt()
                character.scan_char.clear()
                character.transf_char.clear()
                character.position.clear()
                character.current_territory[0]=""
                del self.time
                return "RVLP has been activated"
            else:
                "This subcommand doesn't exist"