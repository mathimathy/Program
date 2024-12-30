from battle.xana_monster import *
#fix data
chr = ["yumi", "aelita", "ulrich", "odd"]
overvehicules=["overbike", "overboard", "overwing"]
territory=["mountain", "ice", "forest", "desert"]
special_territory=["carthage", "replika"]
monsters_surface=[Kankrelat(), Hornet(), Blok(), Krab(), Megatank(), Tarantula()]
monsters_carthage=[Manta(), Creeper()]
special_monster={}

#modifiable data
transf_char=[]
scan_char=[]
virt_char=[]
overvehicules_virt=[]
current_territory = [""]
value = {"isOn": False, "inBattle": False, "inXana": False}
position = []

#XANA DATA
xana_territory=[]
xana_tour=[]