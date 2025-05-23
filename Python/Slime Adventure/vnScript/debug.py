def Run(chars):
    chars["emily"].say("Coucou")
    chars["emily"].choice("Aimes-tu le chocolat ?", [
        ("Oui", saidYes),
        ("Non", saidNo)
    ])(chars)

def saidYes(chars):
    chars["emily"].say("C'est chouette !")

def saidNo(chars):
    chars["emily"].say("Oh dommage...")