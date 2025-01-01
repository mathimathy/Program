from basic.number import *
from basic.op import opposite, absolute

class P:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f'P({self.x},{self.y})'

class D:
    def __init__(self, p1, p2):
        self.p1=p1
        self.p2=p2
    
    def __str__(self):
        return f'D({str(self.p1)},{str(self.p2)})'

class S:
    def __init__(self, p1, p2):
        self.p1=p1
        self.p2=p2
        self.lg = dist(self.p1,self.p2)
    
    def __str__(self):
        return f'S({str(self.p1)},{str(self.p2)})'

def add(a,b):
    if isinstance(a,numberA) and isinstance(b,numberA):
        newId = a.id+b.id
        goodId=newId%8
        newNumber = numberA(goodId)
        numberOfGroup = (newId-goodId)/8
        if numberOfGroup==0:
            result=newNumber
        else:
            result=numberG([newNumber])
        i=1
        while i<numberOfGroup:
            result=numberG([result.n])
        return result
    elif isinstance(a, numberG) and isinstance(b, numberA):
        r = []
        for el in a.n:
            r.append(add(el,b))
        return numberG(r)
    elif isinstance(b, numberG) and isinstance(a, numberA):
        return add(b,a)
    else:
        r=[]
        for i in range(len(a.n)):
            for j in range(len(b.n)):
                r.append(add(a.n[i],b.n[j]))
        return numberG(r)

def dist(a,b):
    if isinstance(a,P) and isinstance(b, P):
        return absolute(add(add(b.x,opposite(a.x)),add(b.y, opposite(a.y))))