import random
import time
def choose_jar(jarres, trousseau, diff):
    jar=input("Numéro de la jarre: ")
    try:
        jar=int(jar)
        if jarres[jar-1]:
            trousseau+=1
            print("gagné")
        else:
            trousseau-=1
            print("piégé")
        time.sleep(1.0)
        main(trousseau, diff)
    except:
        print("vous devez entrer un nombre entre 1 et 5 y compris!")
        time.sleep(1.0)
        choose_jar(jarres, trousseau, diff)
def main(trousseau, diff):
    print('\n'*50)
    print(f"trousseau: {trousseau}")
    if trousseau==3:
        print("Tu deviens roi du temple")
        return
    jarres=[True]*5
    for i in range(diff):
        rand=random.randint(0,4)
        jarres[rand]=False
    choose_jar(jarres, trousseau, diff)
def choix_diff(trousseau):
    try:
        print("\n"*50)
        print("Niveau 1. 1 serpent pour 5 jarres\nNiveau 2. 2 serpent pour 5 jarres\nNiveau 3. 4 serpent pour 5 jarres")
        diff = int(input("choississez une difficultée (1,2,3): "))
        main(trousseau, diff)
    except:
        print("vous devez entrer un nombre entre 1 et 3 y compris!")
if __name__=="__main__":
    trousseau=0
    choix_diff(trousseau)