var = input('Oui ou non: ')
while True:
    if var=="oui":
        print("Youpi on est content")
        break
    elif var=="non":
        print("Oh zut alors !")
        break
    else:
        var=input("OUI OU NON !!!! ")