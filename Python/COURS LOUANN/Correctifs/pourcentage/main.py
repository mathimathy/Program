asking=True
while True:
    try:
        value=float(input("Valeur originelle: "))
        break
    except:
        print("Ca doit être un nombre !")
while asking:
    try:
        pourc = input("Pourcentage: ")
        if pourc=="":
            asking=False
        else:
            value*=1+float(pourc[:-1])/100
            print(value)
    except:
        print("Ca doit être un nombre avec un %")
print(value)