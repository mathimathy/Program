asking=True
value=1
while asking:
    try:
        pourc = input("Pourcentage: ")
        if pourc=="":
            asking=False
        else:
            value*=1+float(pourc)/100
    except:
        pass
print((value-1)*100)