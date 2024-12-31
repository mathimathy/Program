class Vector:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def __add__(self, adder):
        self.x+=adder.x
        self.y+=adder.y
        return self.copy()
    def __mul__(self, mult):
        self.x*=mult
        self.y*=mult
        return self.copy()
    def copy(self):
        return Vector(self.x,self.y)

up=Vector(0,-1)
down=Vector(0,1)
right=Vector(1,0)
left=Vector(-1,0)