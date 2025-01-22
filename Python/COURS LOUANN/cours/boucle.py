# while (répétant tant qu'une condition est remplie)
# while cond:
#	...

compteur = 1
while compteur<100:
	print(compteur)
	compteur+=1

# while True:
#	...

# break -> casse la boucle

#while True:
#	...
#	if cond:
#		break


# for
# for var in range(min=0, max, step=1):
# 	...

for i in range(10): # [min, max[
	print(i)

# Afficher 20x le message "Coucou la famille ça va ?"
# 2 solutions
print("Solution: While")
c = 1
while c<=20:
	print("Coucou la famille ça va ?")
	c+=1

print("Solution: For")
for _ in range(20):
	print("Coucou la famille ça va ?")