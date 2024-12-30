import function as f
try:
	base = f.load_base()
except:
	base_affiche=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
	base = [['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide'],
				['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide'],
				['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide'],
				['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide'],
				['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide'],
				['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide'],
				['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide'],
				['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide'],
				['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide'],
				['vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide','vide']]
def create_base_affiche():
	w=0
	while w <= 9:
		u=0
		while u < len(base[w]):
			if base[w][u] == 'vide':
				base_affiche[w][u] = ' '
			elif base[w][u] == 'th':
				base_affiche[w][u] = '-'
			elif base[w][u] == 'tv':
				base_affiche[w][u] = '|'
			elif base[w][u] == 'crafter':
				base_affiche[w][u] = 'O'
			elif base[w][u] == 'titanium':
				base_affiche[w][u] = 'T'
			elif base[w][u] == 'quartz':
				base_affiche[w][u] = 'Q'
			u+=1
		w+=1
def affiche_base():
	w=0
	print('----------------------')
	while w <= 9:
		x=0
		y='|'
		while x<len(base_affiche[w]):
			y=y+base_affiche[w][x]
			x+=1
		print(y+'|')
		w+=1
	print('----------------------')
def change_base(x,y,name):
	base[x][y] = name