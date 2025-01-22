class Matrice:
    def __init__(self, values):
        self.values=values
        try:
            self.size = (len(values), len(values[0]))
        except:
            self.values=[values]
            self.size = (len(self.values), len(self.values[0]))
    
    def __sizeof__(self):
        return self.size
    
    def __sub__(self, other):
        if self.size==other.size:
            return Matrice([[self.values[i][j]-other.values[i][j] for j in range(self.size[1])] for i in range(self.size[0])])
        else:
            raise ArithmeticError("Doesn't have the same size !")

    def __add__(self, other):
        if self.size==other.size:
            return Matrice([[self.values[i][j]+other.values[i][j] for j in range(self.size[1])] for i in range(self.size[0])])
        else:
            raise ArithmeticError("Doesn't have the same size !")
    
    def __mul__(self, other):
        def subProduct(line, column):
            result=0
            for i in range(len(line)):
                result+=line[i]*column[i]
            return result

        if isinstance(other, Matrice):
            if self.size[1]==other.size[0]:
                return Matrice([
                    [
                        subProduct(self.values[i], [other.values[l][j] for l in range(other.size[0])])
                        for j in range(other.size[1])
                    ] 
                    for i in range(self.size[0])
                ])
            else:
                raise ArithmeticError("Can't do multiplication !")
        else:
            return Matrice([[other*self.values[i][j] for j in range(self.size[1])] for i in range(self.size[0])])
    
    def __rmul__(self, other):
        if not isinstance(other, Matrice):
            return self*other
    
    def __xor__(self, other):
        if self.size==other.size:
            return Matrice([[self.values[i][j]^other.values[i][j] for j in range(self.size[1])] for i in range(self.size[0])])
        else:
            raise ArithmeticError("Doesn't have the same size !")
        
    def __str__(self):
        values = [[str(data) for data in line] for line in self.values]
        out = ""
        for line in values:
            out+=f"|{' '.join(line)}|\n"
        return out
    
    def __call__(self, line, column):
        return self.values[line][column]        

    def __mod__(self, other):
        return Matrice([[data%other for data in line] for line in self.values])

    def inverse(self):
        ...
    
    def identity(self, size):
        ...