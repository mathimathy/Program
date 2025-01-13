# Sécurité (input)
while True:
	try:
		var=int(input("DEMANDE")) # int peut-être remplacé par float et bool
		break
	except:
		print("MESSAGE D'ERREUR")