from random import randint
def tour(x):
	x2 = x*7+1
	x2 = x2*7-4
	return x2
def dix_tour(x):
	return tour(tour(tour(tour(tour(tour(tour(tour(tour(tour(x))))))))))
def itour(x):
	x2 = (x+4)/7
	x2 = (x2-1)/7
	return x2
def idix_tour(x):
	return itour(itour(itour(itour(itour(itour(itour(itour(itour(itour(x))))))))))
def hash(x):
	x=phrase_vers_liste(x)
	x2 = []
	while len(x) != 0:
		x2.append(dix_tour(x[0]))
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
		x2.append(idix_tour(x[0]))
		del x[0]
	x2 = iphrase_vers_liste(x2)
	return x2