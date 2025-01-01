def create_dico(lg):
	with open(f'F:\\programmation\\python\\liste_{lg}.txt', 'r') as fic:
		dico = fic.read().split('\n')
	return dico