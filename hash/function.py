import h1

def hash(x):
	x=phrase_vers_liste(x)
	x2 = []
	while len(x) != 0:
		x2.append(h1.dix_tour(x[0]))
		del x[0]
	return x2

def phrase_vers_liste(phrase):
	c = 0
	r = []
	while c < len(phrase):
		r.append(ord(phrase[c]))
		c+=1
	return r

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
		x2.append(h1.idix_tour(x[0]))
		del x[0]
	x2 = iphrase_vers_liste(x2)
	return x2