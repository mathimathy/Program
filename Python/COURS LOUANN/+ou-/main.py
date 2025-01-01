import random

# Déclaration des variables
en_jeu=True
correcte=False

while en_jeu:
	# Créer un nombre choisi aléatoirement
	nombre_cible = random.randint(0,100)
	while correcte==False:
		nombre = int(input("Insérez un nombre entre 0 et 100: "))
		if nombre==nombre_cible:
			correcte=True
		elif nombre<nombre_cible:
			print("Plus grand !")
		else:
			print("Plus petit !")
	print('Bravo !')
	rejouer=input("Voulez-vous rejouer (oui ou non) ? ")
	if rejouer=="oui":
		correcte=False
	else:
		en_jeu=False