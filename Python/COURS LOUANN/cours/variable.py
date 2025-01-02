# int -> nombre entier (ex: 2,7,-4)

x = 5 # On crée une variable qui s'appelle "x" et qui a la valeur 5
y:int = 2 # On peut sans obligation préciser le type de la variable

# SYNTAXE: nom_de_la_variable(:int) = valeur

# Opérations sur les int (+,-,*,/,**,%)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y) # puissance
print(x%y) # modulo (le reste de la division)



# float -> nombre décimal (ex: 2.7,7.4,-4.3)

x = 5.8 # On crée une variable qui s'appelle "x" et qui a la valeur 5.8
y:float = 2.3 # On peut sans obligation préciser le type de la variable

# SYNTAXE: nom_de_la_variable(:float) = valeur

# Opérations sur les float (+,-,*,/,**,%)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y) # puissance
print(x%y) # modulo (le reste de la division)



# string -> chaîne de caractère (ex: "Coucou", "abcd", "CHOUETTE")

x = "Coucou" # On crée une variable qui s'appelle "x" et qui a la valeur Coucou
y:str = "Comment vas-tu ?" # On peut sans obligation préciser le type de la variable

# SYNTAXE: nom_de_la_variable(:str) = "valeur"

# Opérations sur les string (+, f"", .lower(), .upper(), .replace())
print(x+y) # Concaténisation: on colle les 2 string un à côté de l'autre
print(f"x: {x}, y: {y}") # F-String: permet de mettre la valeur d'une variable dans un string
print(x.lower()) # Met tout en minuscule
print(x.upper()) # Met tout en majuscule
print(x.replace("u", "p")) # Remplace un caractère SYNTAXE: variable.replace(caractère à remplacer, le caractère par lequel on remplace)



# boolean -> vrai ou faux (ex: True, False, 0, 1)

x = True # On crée une variable qui s'appelle "x" et qui a la valeur True
y:bool = False # On peut sans obligation préciser le type de la variable

# SYNTAXE: nom_de_la_variable(:bool) = True ou False

# 1 = True et 0 = False

# Opérations sur les boolean (not, and, or)

print(not x) # Inverse la valeur (True->False, False->True)
print(x and y) # Vaut True si x=True et si y=True sinon vaut False
print(x or y) # Vaut True si au moins x ou y = True