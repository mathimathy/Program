def create_dico(lg):
	with open(f'M:\\PROGRAMMATION\\Program\\Python\\liste_{lg}.txt', 'r') as fic:
		dico = fic.read().split('\n')
	return dico