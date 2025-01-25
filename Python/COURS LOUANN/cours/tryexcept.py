#ZeroDivisionError -> /0
#SyntaxError -> Erreur de syntaxe (oublie d'une parenthèse, d'un :, etc)
#ArithmeticError -> erreur de base pour les calculs:
#	OverflowError -> erreur quand un résultat de calcul est trop grand pour une variable
#	ZeroDivisionError
#	FloatingPointError -> pas utilisé

# pour soulever une exception: raise NomDeLException("msg")
#raise ValueError("AHAH TU ES NUL!")

# pour gérer les exceptions:
# try:
# 	... # on teste le code potentiellement dangereux
# except Error as e:
# 	... # Si Error est levé (renommée e) on exécute ...
# except:
# 	... # Si tout autre erreur est levé, on exécute ...
# else:
# 	... # Si aucune erreur est levée, on exécute ...
# finally:
# 	... # Dans tous les cas, on exécute ...

try:
	x = int(input("Par quoi diviser 20 ? "))
	print(f"{20/x}")
except ZeroDivisionError as zde:
	print("Oulala, vous voulez diviser par 0 ?!?")
except (ValueError, TypeError) as inte:
	print("Vous ne savez qu'on ne peut diviser que par des nombres ?")
except:
	print("\nErreur inattendue")
else:
	print("Bravo, aucune erreur !")
finally:
	print("Au revoir !")