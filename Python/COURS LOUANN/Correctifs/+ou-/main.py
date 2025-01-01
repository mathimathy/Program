import random

def clear():
	print("\n"*50)

BOTTOM=0
TOP=100

clear()
print(f"Bienvenue au jeu du juste prix. Vous devez trouver un nombre que j'aurai choisi entre {BOTTOM} et {TOP}")
input("Appuyez sur Entrer pour continuer...")

while True:
	clear()
	correcte=False
	nombre_cible = random.randint(BOTTOM,TOP)
	print("J'ai choisi un nombre\n")
	while correcte==False:
		try:
			nombre = int(input(f"Insérez un nombre entre {BOTTOM} et {TOP}: "))
			if nombre==nombre_cible:
				correcte=True
			elif nombre==-1:
				print("Merci d'avoir joué !")
				quit()
			elif nombre<nombre_cible:
				print("Plus grand !")
			else:
				print("Plus petit !")
		except:
			print("Vous devez écrire un nombre !")				
	print('Bravo !')
	if input("Voulez-vous rejouer (oui ou non) ? ")=="non":
		print("Merci d'avoir joué !")
		quit()