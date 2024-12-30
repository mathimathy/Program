import random
from classe.command import transf, scan, virt, overvehicule, devirt, rvlp, xana
from classe.character import *
from battle import battle
class Terminal:
    def __init__(self, username):
        self.user = username
        value["isOn"]=True
        self.isOn = value["isOn"]
        self.history = ""
        self.proc={}
        self.proc["transf"]=transf.Transf()
        self.proc["scan"]=scan.Scan()
        self.proc["virt"]=virt.Virt()
        self.proc["overvehicule"]=overvehicule.Overvehicule()
        self.proc["devirt"]=devirt.Devirt()
        self.proc["rvlp"]=rvlp.Rvlp()
        #self.proc["xana"] = xana.Xana()
    def fct_proc(self, cmd):
        try:
            self.history+=self.proc[cmd[0]].run(cmd)+"\n"
        except:
            self.history+="This processus doesn't exist\n"

    def activate_proc(self,proc):
        try:
            self.history += self.proc[proc].init()+"\n"
        except:
            self.history += "This processus doesn't exist\n"
    def traitement_cmd(self,cmd):
        if random.random() >= 0.9 and len(virt_char) != 0:
            value['inBattle']=True
        print('\n'*50)
        cmd = cmd.split('.')
        if cmd[0]=="shutdown":
            self.isOn=False
        elif cmd[0]=="stat":
            self.history+=f"Transf_char: {transf_char}\nscan_char: {scan_char}\nvirt_char: {virt_char}\novervehicule_virt: {overvehicules_virt}\ncurrent_territory: {current_territory}\nposition: {position}\n"
        elif len(cmd) == 1 and cmd[0]!="":
            self.activate_proc(cmd[0])
        elif cmd[0]=="":
            self.history+="\nYou need to type something in the entry !\n"
        else:
            self.fct_proc(cmd)
    def run(self):
        while self.isOn:
            if value["inBattle"]:
                bat = battle.Battle()
                bat.create_monster()
                if bat.turn():
                    pass
                else:
                    self.traitement_cmd(["shutdown"])
            print('\n'*50)
            print(self.history+"\n-----------------------------------------------------")
            cmd = input("> ")
            self.traitement_cmd(cmd)