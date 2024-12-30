import time
from random import *
import pickle
class guerrier:
	def __init__(self, pseudo):
		self.pseudo = pseudo
		self.health = 20
		self.armure = 6
		self.attack1 = 5
		self.attack2 = 10
		self.gold = 10
	def get_pseudo(self):
		return self.pseudo
	def get_health(self):
		return self.health
	def get_armure(self):
		return self.armure
	def get_attack1(self):
		return self.attack1
	def get_attack2(self):
		return self.attack2
	def get_gold(self):
		return self.gold
	def dammage(self, dammage):
		if self.armure > 0:
			self.armure -= 1
			dammage = 0
		self.health -= dammage
	def blade(self):
		self.armure = 6
	def blade_health(self):
		self.health = 20
	def achat(self, price):
		if self.gold > price:
			self.gold -= price
			return "true"
		else:
			return "false"
	def pay(self, price):
		self.gold += price
class sorcier:
	def __init__(self, pseudo):
		self.pseudo = pseudo
		self.health = 15
		self.armure = 2
		self.attack1 = 7
		self.attack2 = 14
		self.gold = 10
	def get_pseudo(self):
		return self.pseudo
	def get_health(self):
		return self.health
	def get_armure(self):
		return self.armure
	def get_attack1(self):
		return self.attack1
	def get_attack2(self):
		return self.attack2
	def get_gold(self):
		return self.gold
	def dammage(self, dammage):
		if self.armure > 0:
			self.armure -= 1
			dammage = 0
		self.health -= dammage
	def blade(self):
		self.armure = 2
	def blade_health(self):
		self.health = 15
	def achat(self, price):
		if self.gold > price:
			self.gold -= price
			return "true"
		else:
			return "false"
	def pay(self, price):
		self.gold += price
class templier:
	def __init__(self, pseudo):
		self.pseudo = pseudo
		self.health = 22
		self.armure = 5
		self.attack1 = 4
		self.attack2 = 8
		self.gold = 10
	def get_pseudo(self):
		return self.pseudo
	def get_health(self):
		return self.health
	def get_armure(self):
		return self.armure
	def get_attack1(self):
		return self.attack1
	def get_attack2(self):
		return self.attack2
	def get_gold(self):
		return self.gold
	def dammage(self, dammage):
		if self.armure > 0:
			self.armure -= 1
			dammage = 0
		self.health -= dammage
	def blade(self):
		self.armure = 5
	def blade_health(self):
		self.health = 22
	def achat(self, price):
		if self.gold > price:
			self.gold -= price
			return "true"
		else:
			return "false"
	def pay(self, price):
		self.gold += price
def jeu_b(attack1b, attack2b, bot, player, d):
	attack = randint(1, 2)
	if attack == 1:
			attack1_degat = bot.get_attack1()
			player.dammage(attack1_degat)
			print("bot attaque", attack1b)
	elif attack == 2:
		if d == 1:
			attack2_degat = bot.get_attack2()
			player.dammage(attack2_degat)
			print("bot attaque", attack2b)
			d -= 1
			return d
		elif d == 2:
			attack2_degat = bot.get_attack2()
			player.dammage(attack2_degat)
			print("bot attaque", attack2b)
			d -= 1
			return d
		elif d == 3:
			attack2_degat = bot.get_attack2()
			player.dammage(attack2_degat)
			print("bot attaque", attack2b)
			d -= 1
			return d
		else:
			attack1_degat = bot.get_attack1()
			player.dammage(attack1_degat)
			print("bot attaque", attack1b)
def clear():
	print("\n" * 50)
def verify(pseudo):
	len_pseudo = len(pseudo)
	if len_pseudo == 0:
		return 'false'
	else:
		return 'true'
def game_over(health, bot_health, e, a, d, db, ddb, player, race, raceb, attaque1, attaque2):
	if health == 0 and bot_health != 0 and bot_health > 0 or health < 0 and bot_health != 0 and bot_health > 0:
		print('Game Over')
		responce = input('Voulez vous recommancer ? (oui, non) ')
		if responce == 'oui':
			return 1, 1, 1, ddb
		elif responce == 'non':
			save(player, "0", race, attaque1, attaque2)
			quit()
	else:
		return 2, 1, d, db
def win(bot_health, health, e, a, d, db, ddb, player, dificult, race, raceb, attaque1, attaque2):
	if bot_health == 0 and health != 0 and health > 0 or bot_health < 0 and health != 0 and health > 0:
		print('You Win')
		if raceb == 'sorcier':
			player.pay(2)
		elif raceb == 'templier':
			player.pay(4)
		elif raceb == 'guerrier':
			player.pay(5)
		responce = input('Voulez vous recommancer ? (oui, non) ')
		if responce == 'oui':
			return 1, 1, 1, ddb
		elif responce == 'non':
			save(player, dificult, race, attaque1, attaque2)
			quit()
	else:
		return 2, 1, d, db
def save(player, dificult, race, attaque1, attaque2):
	attaque2 = "\n" + attaque2
	with open("player.save", "wb") as fic:
		record = pickle.Pickler(fic)
		record.dump(player)
	with open("dificult.save", "w") as fic:
		fic.write(dificult)
	with open("race.save", "w") as fic:
		fic.write(race)
	with open("attaque.save", "w") as fic:
		fic.write(attaque1)
		fic.write(attaque2)
def load():
	with open("player.save", "rb") as fic:
		get_record = pickle.Unpickler(fic)
		player = get_record.load()
	with open("dificult.save", "r") as fic:
		dificult = fic.read()
	with open("race.save", "r") as fic:
		race = fic.read()
	with open("attaque.save", "r") as fic:
		attaque1 = fic.readline()
		attaque2 = fic.readline()
	return player, dificult, race, attaque1, attaque2
e = 1
a = 1
d = 1
db = 0
c = 1
f = 1
g = 1
ddb = 0
try:
	player, dificult, race, attaque1, attaque2 = load()
	if dificult == "0":
		b + "a"
except:
	while f == 1:
		clear()
		dificult = input("Choix de la dificultée: facile, moyen ou difficile ? ")
		if dificult == 'facile':
			ddb = 1
			f = 2
			price = 2
		elif dificult == 'moyen':
			ddb = 2
			f = 2
			price = 4
		elif dificult == 'difficile':
			ddb = 3
			f = 2
			price = 5
		else:
			print('cette dificultée n\'existe pas')
			time.sleep(1)
		db = ddb
	while c == 1:
			clear()
			pseudo = input("Quel est votre pseudo ? ")
			b = verify(pseudo)
			if b == 'true':
				c = 2
			elif b == 'false':
				pass
	while g == 1:
		clear()
		race = input("Que voulez vous etre (guerrier, sorcier, templier) ? ")
		if race == 'guerrier':
			player = guerrier(pseudo)
			attaque1 = "tranche"
			attaque2 = "piquéer"
			g = 2
		elif race == 'sorcier':
			player = sorcier(pseudo)
			attaque1 = "boule de feu"
			attaque2 = "glaciation"
			g = 2
		elif race == 'templier':
			player = templier(pseudo)
			attaque1 = "coup de bouclier"
			attaque2 = "fendoir"
			g = 2
		else:
			print("ce personnage n'existe pas")
			time.sleep(1)
finally:
	if dificult == 'facile':
		ddb = 1
		f = 2
		price = 2
	elif dificult == 'moyen':
		ddb = 2
		f = 2
		price = 4
	elif dificult == 'difficile':
		ddb = 3
		f = 2
		price = 5
	db = ddb
	print("Bienvenu", player.get_pseudo())
	time.sleep(2)
	clear()
	while e == 1:
		clear()
		raceb = randint(1, 3)
		if raceb == 1:
			bot = guerrier("")
			raceb = 'guerrier'
			attack1b = "tranche"
			attack2b = "piquéer"
		elif raceb == 2:
			bot = sorcier("")
			raceb = 'sorcier'
			attack1b = "boule de feu"
			attack2b = "glaciation"
		elif raceb == 3:
			bot = templier("")
			raceb = 'templier'
			attack1b = "coup de bouclier"
			attack2b = "fendoir"
		clear()
		while a == 1:
			commande = input("Que voulez vous faire ? ")
			if commande == 'quitter':
				save(player, dificult, race, attaque1, attaque2)
				quit()
			elif commande == 'stat':
				clear()
				print(race)
				print("vie", player.get_health())
				print("armure", player.get_armure())
				print("or", player.get_gold())
			elif commande == 'statb':
				clear()
				print(raceb)
				print("vie", bot.get_health())
				print("armure", bot.get_armure())
			elif commande == 'attaquer':
				clear()
				attack = input("Quel attaque voulez vous faire (1: {}, 2: {}) ? ". format(attaque1, attaque2))
				if attack == '1':
					attack1_degat = player.get_attack1()
					bot.dammage(attack1_degat)
					print(player.get_pseudo(), "attaque", attaque1)
					db = jeu_b(attack1b, attack2b, bot, player, db)
				elif attack == '2':
					if d != 0: 
						attack2_degat = player.get_attack2()
						bot.dammage(attack2_degat)
						print(player.get_pseudo(), "attaque", attaque2)
						d -= 1
						db = jeu_b(attack1b, attack2b, bot, player, db)
					else:
						print('Vous ne pouvez plus utiliser cette attaque !')
			elif commande == 'blade':
				boolean = player.achat(price)
				if boolean == 'true':
					player.blade()
					print('Achat reussi !!')
				elif boolean == 'false':
					print('Vous n\'avez pas assez d\'argent pour l\'acheter !!')
			elif commande == 'potion':
				price = price + 2
				boolean = player.achat(price)
				if boolean == 'true':
					player.blade_health()
					print('Achat reussi !!')
				elif boolean == 'false':
					print('Vous n\'avez pas assez d\'argent pour l\'acheter !!')
			elif commande == '^[[A^[[A^[[C^[[D^[[B^[[A':
				code = input('Code d\'acsses ')
				if code == '$Root$596247318$Root$':
					print('astuces: il parait que quand on attaque pas avec la 2 pendant l\'armure on a plus de chance de gagner :)')
				else:
					print('code d\'acsses invalide !')
			elif commande == 'help':
				clear()
				print('quitter = permet de quitter le jeu')
				print('attaquer = permet d\'attaquer')
				print('stat = permet d\'afficher vos stat')
				print('statb = permet d\'afficher les stat du bot')
				print('blade = permet de recharger les point d\'armure')
				print('potion = permet de recharger sa vie')
			else:
				print("ce que vous essayez de faire n'est pas possible utiliser \'help\' pour avoir de l'aide")
			health = player.get_health()
			bot_health = bot.get_health() 
			e, a, d, db = game_over(health, bot_health, e, a, d, db, ddb, player, race, raceb, attaque1, attaque2)
			e, a, d, db = win(bot_health, health, e, a, d, db, ddb, player, dificult, race, raceb, attaque1, attaque2)