import data as d
def craft_item(name_item):
	dico = d.craft_item[name_item]
	dico_keys = dico.keys()
	if dico_keys in d.inventory_object.keys():
		i=0
		while i < len(dico_keys):
			if dico[dico_keys[i]] < d.inventory_object[dico_keys[i]]:
				d.inventory_object[dico_keys[i]] -= dico[dico_keys[i]]
				if name_item in d.inventory_object.keys():
					d.inventory_object[name_item]+=1
				else:
					d.inventory_object[name_item] = 1
				return True
			elif dico[dico_keys[i]] == d.inventory_object[dico_keys[i]]:
				del d.inventory_object[dico_keys[i]]
				if name_item in d.inventory_object.keys():
					d.inventory_object[name_item]+=1
				else:
					d.inventory_object[name_item] = 1
				return True
			else:
				return False
def craft_tool(name_item):
	dico = d.craft_tool[name_item]
	dico_keys = dico.keys()
	if dico_keys in d.inventory_object.keys():
		i=0
		while i < len(dico_keys):
			if dico[dico_keys[i]] < d.inventory_object[dico_keys[i]]:
				d.inventory_object[dico_keys[i]] -= dico[dico_keys[i]]
				if name_item in d.inventory_tool.keys():
					d.inventory_tool[name_item]+=1
				else:
					d.inventory_tool[name_item] = 1
				return True
			elif dico[dico_keys[i]] == d.inventory_object[dico_keys[i]]:
				del d.inventory_object[dico_keys[i]]
				if name_item in d.inventory_tool.keys():
					d.inventory_object[name_item]=1
				else:
					d.inventory_tool[name_item] = 1
				return True
			else:
				return False
def craft_equi(name_item):
	dico = d.craft_tool[name_item]
	dico_keys = dico.keys()
	if dico_keys in d.inventory_object.keys():
		i=0
		while i < len(dico_keys):
			if dico[dico_keys[i]] < d.inventory_object[dico_keys[i]]:
				d.inventory_object[dico_keys[i]] -= dico[dico_keys[i]]
				if name_item in d.inventory_equi.keys():
					d.inventory_object[name_item]=1
				else:
					d.inventory_equi[name_item] = 1
				return True
			elif dico[dico_keys[i]] == d.inventory_object[dico_keys[i]]:
				del d.inventory_object[dico_keys[i]]
				if name_item in d.inventory_equi.keys():
					d.inventory_object[name_item]=1
				else:
					d.inventory_equi[name_item] = 1
				return True
			else:
				return False