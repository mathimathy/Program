import numpy as np
def itour(x):
	x2 = x+4
	x2=x2/7
	x2 = x2-1
	x2=x2/7
	return x2

def idix_tour(x):
	return np.round(itour(itour(itour(itour(itour(itour(itour(itour(itour(itour(x)))))))))))

def iphrase_vers_liste(phrase):
	c = 0
	r=''
	while c < len(phrase):
		r=r+(chr(int(phrase[c])))
		c+=1
	return r

def ihash(x):
	x2 = []
	while len(x) != 0:
		x2.append(idix_tour(x[0]))
		del x[0]
	x2 = iphrase_vers_liste(x2)
	return x2

with open('ci.txt', 'r') as fic:
	prenom = fic.readline().split(',')
	nom = fic.readline().split(',')
	age = fic.readline().split(',')
	sexe = fic.readline().split(',')
	n = fic.readline().split(',')
	an = fic.readline().split(',')
	ddn = fic.readline().split(',')
	ldn = fic.readline().split(',')
c=0
while c < len(prenom):
	prenom[c] = int(prenom[c])
	c+=1
c=0
while c < len(nom):
	nom[c] = int(nom[c])
	c+=1
c=0
while c < len(age):
	age[c] = int(age[c])
	c+=1
c=0
while c < len(sexe):
	sexe[c] = int(sexe[c])
	c+=1
c=0
while c < len(n):
	n[c] = int(n[c])
	c+=1
c=0
while c < len(an):
	an[c] = int(an[c])
	c+=1
c=0
while c < len(ddn):
	ddn[c] = int(ddn[c])
	c+=1
c=0
while c < len(ldn):
	ldn[c] = int(ldn[c])
	c+=1

prenom = ihash(prenom)
nom = ihash(nom)
age = ihash(age)
sexe = ihash(sexe)
n = ihash(n)
an = ihash(an)
ddn = ihash(ddn)
ldn = ihash(ldn)

print('Prénom: ' + prenom + 
	'\nNom: ' + nom + 
	'\nAge: ' + age + 
	'\nSexe: ' + sexe + 
	'\nNationalitée: ' + n +
	'\nAutre nom: ' + an + 
	'\nDate de naiscence: ' + ddn + 
	'\nLieu de naiscence: ' + ldn)
while True:
	pass