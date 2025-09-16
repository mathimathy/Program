class Interpreter:
    def __init__(self, file):
        self.path = "/".join(file.split("/")[:-1])
        self.mdef = self.readMainDef(file)
        self.var = {}
    
    def readMainDef(self, file):
        if file[-5:]==".mdef":
            with open(file, "r") as f:
                mainDef = f.read()
            mainDef = mainDef.replace(" ", "").replace("\t", "").replace("\n}", "").replace('{\n', "").replace(",\n", " ").replace("\"", "").split("\n")
            result=[]
            for el in mainDef:
                newEl = el.split(":")
                r = []
                for el in newEl:
                    r.append(el.split(" "))
                result.append(r)
            dictResult = {}
            for el in result:
                dictResult[el[0][0]]=el[1:][0]
            dictResult["mainFile"]=dictResult['mainFile'][0]
            dicInterValue={}
            for el in dictResult["funcName"]:
                interValue=el.split("->")
                dicInterValue[interValue[0]]=interValue[1]
            dictResult["funcName"]=dicInterValue
            return dictResult
    
    def readDef(self, file):
        if file[-4:]==".def":
            with open(self.path+"/"+file, "r") as f:
                definitions = f.read()
            definitions = definitions.replace(" ", "").split("\n")
            result={}
            for el in definitions:
                newEl = el.split("->")
                result[newEl[0]]=newEl[1]
            return result
    
    def runFunc(self, name):
        id=int(self.mdef["funcName"][name])
        definition = self.readDef(self.mdef["funcDef"][id])
        lines = definition[name].split("/")
        lineStart=lines[0]
        lineEnd=lines[1]
        self.runFile(self.mdef["funcFile"][id], lineStart, lineEnd)
    
    def main(self):
        self.runFile("main.ph")
            
    def runFile(self, fileName, lineStart=0, lineEnd=""):
        if fileName[-3:]==".ph":
            with open(self.path+"/"+fileName, "r") as f:
                code = f.read().split("\n")
                if lineEnd=="":
                    code=code[int(lineStart):]
                else:
                    code=code[int(lineStart):int(lineEnd)+1]
            for line in code:
                self.execute(line)
    
    def execute(self, line):
        cmd = line.split(" ")
        if cmd[0]=="call":
            self.runFunc(cmd[1])
        elif cmd[1]=="=":
            self.var[cmd[0]]=self.evaluate(cmd[2])
        elif cmd[0]=="print":
            if cmd[1] in self.var.keys():
                print(self.var[cmd[1]])
            else:
                print(self.evaluate(cmd[1]))

    def evaluate(self, exp):
        if exp[0]=='"' and exp[-1]=='"':
            return exp[1:-1]
        else:
            try:
                return float(exp)
            except:
                if "+" in exp:
                    result=""
                    resultN=0
                    exp=exp.split("+")
                    for el in exp:
                        if el[0]=='"' and el[-1]=="":
                            result+=el[1:-1]
                        elif el in self.var.keys():
                            if isinstance(self.var[el], str):
                                result+=self.var[el]
                            else:
                                resultN+=self.var[el]
                        else:
                            resultN+=float(el)
                    if result=="":
                        return resultN
                    else:
                        return result
                elif "-" in exp:
                    result=""
                    resultN=0
                    exp=exp.split("-")
                    for el in exp:
                        if el in self.var.keys():
                            if el==exp[0]:
                                resultN+=self.var[el]
                            else:
                                resultN-=self.var[el]
                        else:
                            if el==exp[0]:
                                resultN+=self.var[el]
                            else:
                                resultN-=self.var[el]
                    return resultN
                elif "*" in exp:
                    resultN=0
                    exp=exp.split("*")
                    for el in exp:
                        if el in self.var.keys():
                            if el==exp[0]:
                                resultN+=self.var[el]
                            else:
                                resultN*=self.var[el]
                        else:
                            if el==exp[0]:
                                resultN+=self.var[el]
                            else:
                                resultN*=self.var[el]
                    return resultN
                elif "/" in exp:
                    resultN=0
                    exp=exp.split("/")
                    for el in exp:
                        if el in self.var.keys():
                            if el==exp[0]:
                                resultN+=self.var[el]
                            else:
                                resultN/=self.var[el]
                        else:
                            if el==exp[0]:
                                resultN+=self.var[el]
                            else:
                                resultN/=self.var[el]
                    return resultN
                elif "%" in exp:
                    resultN=0
                    exp=exp.split("%")
                    for el in exp:
                        if el in self.var.keys():
                            if el==exp[0]:
                                resultN+=self.var[el]
                            else:
                                resultN%=self.var[el]
                        else:
                            if el==exp[0]:
                                resultN+=self.var[el]
                            else:
                                resultN%=self.var[el]
                    return resultN

if __name__=="__main__":
    inter = Interpreter("test/main.mdef")
    inter.main()