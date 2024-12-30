def tour(x):
	x2 = x*7+1
	x2 = x2*7-4
	return x2
def dix_tour(x):
	return tour(tour(tour(tour(tour(tour(tour(tour(tour(tour(x))))))))))
def hash(x):
	x2 = ''
	while len(x)-1 != 0:
		x2=x2+str((dix_tour(x[0])))+','
		del x[0]
	x2=x2+str((dix_tour(x[0])))
	return x2
def phrase_vers_liste(phrase):
	c = 0
	r = []
	while c < len(phrase):
		r.append(ord(phrase[c]) % 100)
		c+=1
	return r
with open('ci.txt', 'w+') as fic:
	fic.write(str(hash(phrase_vers_liste(input('Prénom: ')))) + '\n')
	fic.write(str(hash(phrase_vers_liste(input('Nom: ')))) + '\n')
	fic.write(str(hash(phrase_vers_liste(input('Age: ')))) + '\n')
	fic.write(str(hash(phrase_vers_liste(input('Sexe: ')))) + '\n')
	fic.write(str(hash(phrase_vers_liste(input('Nationalitée: ')))) + '\n')
	fic.write(str(hash(phrase_vers_liste(input('Autre Nom: ')))) + '\n')
	fic.write(str(hash(phrase_vers_liste(input('Date de naiscence: ')))) + '\n')
	fic.write(str(hash(phrase_vers_liste(input('Lieu de naiscence: ')))) + '\n')