import copy
class Var:
	def __init__(self, value=None):
		self.value=copy.deepcopy(value)
		self.type=type(self.value)

	def set(self, value):
		self.value=copy.deepcopy(value)
		self.type=type(self.value)

	def get(self, index=None):
		if self.getType()==type([]) or self.getType()==type({}):
			if index!=None:
				return self.value[index]
		return self.value

	def append(self, item):
		if self.getType()==type([]):
			self.value.append(item)

	def remove(self, key=-1):
		if self.getType()==type([]) or self.getType()==type({}):
			del self.value[key]

	def add(self, index, value):
		if self.getType()==type({}):
			self.value[index]=copy.deepcopy(value)

	def getType(self):
		return self.type

	def __add__(self, other):
		if type(other)==type(self):
			if self.getType()==type([]):
				result=Var()
				result.set(self.get())
				if other.getType()==type([]):
					for el in other.get():
						result.append(el)
				elif other.getType()==type({}):
					for el in other.get().values():
						result.append(el)
				else:
					result.append(other.get())
			elif self.getType()==type({}):
				pass
			else:
				result=Var()
				result.set(other.get())
				if other.getType()==type([]):
					result.append(self.get())
				elif other.getType()==type({}):
					pass
				else:
					try:
						result.set(self.get()+result.get())
					except:
						result.set(str(self.get())+str(result.get()))
		return result