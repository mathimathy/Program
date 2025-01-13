from mod.character import Character

def Run(chars: dict[str, Character]):
    chars["emily"].say("Coucou")
    chars["emily"].choice("Aimes-tu le chocolat ?", [
        ("Oui", saidYes),
        ("Non", saidNo)
    ])(chars)

def saidYes(chars):
    chars["emily"].say("C'est chouette !")

def saidNo(chars):
    chars["emily"].say("Oh dommage...")