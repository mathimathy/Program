import math
from basic.number import *
def starSimple(aN, bN):
    a=aN.id
    b=bN.id
    op = [[e,v,w,x,y,z,m,n],
            [v,e,y,w,v,x,m,n],
            [w,y,e,z,v,y,m,n],
            [x,w,z,e,w,w,m,n],
            [y,v,v,w,e,x,m,n],
            [z,x,y,w,x,e,m,n],
            [m,m,m,m,m,m,None,None],
            [n,n,n,n,n,n,None,None]]
    invOp = [[e,v,w,x,y,z,opposite(m),opposite(n)],
                [v,numberP([e,y]),y,opposite(z),numberP([v,w]),None,opposite(m),opposite(n)],
                [w,x,e,numberP([v,y,z]),x,x,opposite(m),opposite(n)],
                [x,z,numberP([opposite(v),opposite(y),opposite(z)]),e,z,numberP([v,y]),opposite(m),opposite(n)],
                [y,w,numberP([v,z]),opposite(z),e,w,opposite(m),opposite(n)],
                [z,None,x,w,opposite(w),e,opposite(m),opposite(n)],
                [m,m,m,m,m,m,numberP([e,v,w,x,y,z]),numberP([e,v,w,x,y,z])],
                [n,n,n,n,n,n,numberP([e,v,w,x,y,z]),numberP([e,v,w,x,y,z])]]
    if a>=0 and b>=0:
        return op[a][b]
    elif a<0 and b<0:
        return opposite(starSimple(opposite(aN),opposite(bN)))
    elif a<0:
        return invOp[b][-a]
    elif b<0:
        return invOp[a][-b]

def star(a,b):
    if isinstance(a,numberA) and isinstance(b,numberA):
        return starSimple(a,b)
    elif isinstance(a,numberA):
        return star(b,a)
    elif isinstance(a,numberG):
        data=[]
        for el in a.n:
            data.append(star(el,b))
        return numberG(data)
    else:
        data=[]
        for el in a.n:
            data.append(star(el,b))
        return numberP(data)

def oppositeSimple(a):
    n = numberA(str(a))
    n.id*=-1
    return n

def opposite(a):
    if isinstance(a,numberA):
        return oppositeSimple(a)
    elif isinstance(a,numberG):
        data=[]
        for el in a.n:
            data.append(opposite(el))
        return numberG(data)
    else:
        data=[]
        for el in a.n:
            data.append(opposite(el))
        return numberP(data)

    

def triangleSimple(aN, bN):
    a = aN.id
    b = bN.id
    op = [[e,e,e,e,e,e,e,e],
              [e,z,y,v,w,m,y,w],
              [e,y,v,w,m,z,n,y],
              [e,v,w,x,y,z,m,n],
              [e,w,m,y,m,v,z,y],
              [e,m,z,z,v,w,v,n],
              [e,y,n,m,z,n,n,w],
              [e,w,y,n,y,n,w,v]]
    invOp = [[numberP([e,b,w,x,y,z,m,n]),e,e,e,e,e,e,e],
                [None,x,w,v,z,numberP([y,m]),opposite(z),n],
                [None,numberP([y,n]),x,w,v,z,n,numberP([v,m])],
                [None,opposite(v),opposite(w),x,opposite(y),opposite(z),opposite(m),opposite(n)],
                [None,numberP([w,m]),numberP([v,n]),y,numberP([x,n]),opposite(m),v,numberP([w,y])],
                [None,v,z,z,m,numberP([w,x]),y,opposite(n)],
                [None,z,y,m,numberP([w,y]),v,x,numberP([opposite(w),opposite(z),opposite(m)])],
                [None,opposite(n),m,n,numberP([opposite(w),opposite(y)]),n,numberP([w,z,m]),numberP([x,z])]]
    if a>=0 and b>=0:
        return op[a][b]
    elif a<0 and b<0:
        return opposite(triangleSimple(opposite(aN),opposite(bN)))
    elif a<0:
        return invOp[b][-a]
    elif b<0:
        return invOp[a][-b]

def triangle(a,b):
    if isinstance(a,numberA) and isinstance(b,numberA):
        return triangleSimple(a,b)
    elif isinstance(a,numberA):
        return triangle(b,a)
    elif isinstance(a,numberG):
        data=[]
        for el in a.n:
            data.append(triangle(el))
        return numberG(data)
    else:
        data=[]
        for el in a.n:
            data.append(triangle(el))
        return numberP(data)

def circle(*args):
    return numberG(args)

def square(*args):
    return numberP(args)

def absolute(a):
    if isinstance(a,numberA):
        return numberA(math.abs(a.id))