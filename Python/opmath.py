from mpmath import *
from sympy import integrate,Symbol,oo
c=299792458
gt=9.81
gl=1.622
gme=3.7
gma=3.711
gv=8.87
gj=24.79
gs=10.44
gu=8.87
gn=11.15
gp=0.62
x=Symbol('x')
def premier(n):
	a = 2
	b = True
	while a <= sqrt(n):
		if n%a == 0:
			b = False
		a+=1
	return b
def premiers(n):
	x = []
	c = 2
	while c < n:
		if premier(c):
			x.append(c)
			c+=1
		else:
			c+=1
	return x
def F(f):
	print(integrate(f,x))
def integral(a,b,f):
	return f(b)-f(a)
def sigma(vn,jc,f):
	result=0
	try:
		for i in range(vn,jc+1):
			result+=f(i)
	except:
		i=vn
		while i < jc:
			result+=f(i)
	return result
def PI(vn,jc,f):
	result=1
	for i in range(vn,jc+1):
		result*=f(i)
	return result
def fact(n):
	f=lambda x :x
	result = PI(1,n,f)
	return result
def cb(k,n):
	result = fact(n)/(fact(k)*fact(n-k))
	return result
def pi(m):
	f=lambda x :(((x-1)*2+1)/x)-((x-1)/x)
	result=sigma(2,m,f)
	return result
def Ec(m,v):
	return 1/2*m*v**2
def P(m,g):
	return m*g
def a(sf,m):
	return sf/m
def v(d,t):
	return d/t
def Em(Ec,Epp):
	return Ec+Epp
def Epp(m,g,zg):
	return m*g*zg
def E(m):
	return m*c**2
def m(E):
	return E/c**2
def rho(m,vol):
	return m/vol
def fib(n):
	a,b = 1,1
	x=[]
	while len(x) <= n:
		b,a=a+b,b
		x.append(a)
	x.append(b)
	return x
def PGCD(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return PGCD(b,r)
def PPCM(a,b):
    if (a==0) or (b==0):
        return 0
    else:
        return (a*b)//PGCD(a,b)
def lookAndSay(n):
    def conway(z):
        zz, old, c =[], z[0], 0 # c = compteur
        for i in range(len(z)):
            if z[i]!=old:
                zz+=[c]+[old]
                old, c = z[i], 1
            else :
                c+=1
        return zz+[c]+[old]
    z=[1]
    for _ in range(n-1):
        z=conway(z)
    return ''.join(str(i) for i in z)