import data as d
import base_creator as b
def save():
	with open('save/data.save', 'w+') as fic:
		fic.write(d.inventory_object)
		fic.write(d.inventory_tool)
		fic.write(d.tool_activate)
		fic.write(d.inventory_equi)
	with open('save/base.save', 'w+') as fic:
		fic.write(b.base)
def load():
	with open('save/data.save', 'r') as fic:
		inventory_object = fic.readline()
		inventory_tool = fic.readline()
		tool_activate = fic.readline()
	return inventory_object, inventory_tool, tool_activate
def load_base():
	with open('save/base.txt', 'r') as fic:
		base = fic.readline()
	return base
def clear():
	print('\n'*50)