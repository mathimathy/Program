import sys
class Data:
    def __init__(self, modules={}):
        self.modules = modules

    def save(self, data):
        ...
    
    def load(self, path):
        data = {}
        def read(code):
            d= {}
            counter = 0
            while counter<len(code):
                line = code[counter]
                line = line.strip()
                if (x:=line.split(" "))[0]=="using":
                    __import__(x[1])
                    self.modules[x[1]]=sys.modules[x[1]].data
                    counter+=1
                    continue
                elif ": " in line:
                    line = line.split(": ")
                elif ":" in line:
                    line = line.split(":")
                else:
                    counter+=1
                    continue
                d[line[0]], counter=value(line[1], counter, code)
            return d
        def value(v, c, code):
            if v[0]=='"' and v[-1]=='"':
                return v[1:-1], c+1
            elif "." in v:
                v = v.split(".")
                return self.modules[v[0]](v[1]), c+1
            elif v=="{":
                counter=0
                for index, line in enumerate(code[c:]):
                    if line.strip()[-1]=="{":
                        counter+=1
                    if line.strip()=="}":
                        counter-=1
                    if counter==0:
                        jmp=index
                        break
                return read(code[c+1:c+jmp]), c+jmp+1
            elif "," in v:
                return float(v.replace(",",".")), c+1
            else:
                return int(v), c+1
            
        with open(path) as f:
            code = f.read().split("\n")
            data = read(code)
        return data

if __name__=="__main__":
    d=Data()
    data = d.load("exemple.data")
    print(data)