class numberA:
    def __init__(self, name):
        if isinstance(name, str):
            invert=1
            self.id=0
            if len(name)==2:
                invert=-1
                name=name[:-1]
            if name=="v":
                self.id = 1
            elif name=="w":
                self.id = 2
            elif name=="x":
                self.id = 3
            elif name=="y":
                self.id = 4
            elif name=="z":
                self.id = 5
            elif name=="e":
                self.id = 0
            elif name=="m":
                self.id = 6
            elif name=="n":
                self.id = 7
            self.id*=invert
        else:
            self.id=name

    
    def __str__(self):
        match self.id:
            case 0:
                return "e"
            case 1:
                return "v"
            case 2:
                return "w"
            case 3:
                return "x"
            case 4:
                return "y"
            case 5:
                return "z"
            case 6:
                return "m"
            case 7:
                return "n"
        match -self.id:
            case 0:
                return "e/"
            case 1:
                return "v/"
            case 2:
                return "w/"
            case 3:
                return "x/"
            case 4:
                return "y/"
            case 5:
                return "z/"
            case 6:
                return "m/"
            case 7:
                return "n/"
            

class numberG:
    def __init__(self, n):
        self.n=n
    
    def __str__(self):
        toPrint=[]
        for el in self.n:
            toPrint.append(str(el))
        return str(toPrint).replace('[', '{').replace(']', '}')

class numberP:
    def __init__(self,n):
        self.n=n

    def __str__(self):
        toPrint=[]
        for el in self.n:
            toPrint.append(str(el))
        return str(toPrint)

v = numberA("v")
w = numberA("w")
x = numberA("x")
y = numberA("y")
z = numberA("z")
e = numberA("e")
n = numberA("n")
m = numberA("m")