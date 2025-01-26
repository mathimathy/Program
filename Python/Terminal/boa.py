import sys
import os
import pickle
import time

class parentObj:
	def __init__(self, inter):
		self.var={}
		self.func={}
		self.inter=inter
	
	def addFunc(self, name, file):
		self.func[name]=(Interpreter(self.inter.home, self.inter.stack, True, self),file)
	
	def get(self, var):
		return self.var[var]
	
	def ret(self, v, var):
		self.var[var]=v
	
	def callFunc(self, name):
		self.func[name][0].read(self.func[name][1])

class Stack:
    def __init__(self):
        self._d = []
    
    def push(self, value):
        self._d.append(value)
    
    def pop(self):
        if len(self._d)>0:
            data = self._d[-1]
            del self._d[-1]
            return data
        else:
            raise IndexError("You're trying to pop the stack but it's empty")
    
    def empty(self):
        self._d=[]

class Interpreter:

	def __init__(self, home, stack=Stack(), objFunc=False, parentObj=None):
		self.home=home
		self.cmd=None
		self.jmpPt=[]
		self.error=None
		self.var={}
		self.cursor=0
		self.code=None
		self.fctAdress={}
		self.inFct=False
		self.cond=0
		self.callAdress=None
		self.object={}
		self.stack=stack
		self.objFunc=objFunc
		self.parentObj=parentObj

	def interprete(self, line):
		if line=="/":
			if self.cmd==7:
				if os.path.isfile(self.home+"out.bdata"):
					with open(self.home+"out.bdata", "rb") as f:
						self.stack = pickle.load(f)
				else:
					self.stack.empty()
			else:
				if len(self.jmpPt)==0:
					self.cursor=len(self.code)
				else:
					del self.jmpPt[-1]
		elif line=="":
			pass
		elif line[:2]=="//":
			pass
		elif (l:=line.split(" "))[0]=="get" and self.objFunc:
			self.var[l[1]]=self.parentObj.get(l[1])
		elif (l:=line.split(" "))[0]=="ret" and self.objFunc:
			v=l[1].split("->")
			self.parentObj.ret(self.var[v[0]], v[1])
		elif line=="}":
			if self.inFct and self.cond==0:
				self.cursor=self.callAdress
				self.inFct=False
			else:
				self.cond-=1
		elif line=="[":
			self.jmpPt.append(self.cursor)
		elif line=="]":
			if self.jmpPt==[]:
				pass
			else:
				self.cursor=self.jmpPt[-1]
		elif line[0]=="(":
			if self.cmd==3:
				if line[2]==".":
					if int(self.var[line[1]])!=int(self.var[line[3]]):
						i=self.cursor
						number=0
						while i<len(self.code):
							if len(self.code[i])>1:
								if self.code[i][-1]=="{":
									number+=1
							if self.code[i]=="}":
								number-=1
							if number==0:
								self.cursor=i
								return
							i+=1
					self.cond+=1
				elif line[2]==",":
					if int(self.var[line[1]])>=int(self.var[line[3]]):
						i=self.cursor
						number=0
						while i<len(self.code):
							if len(self.code[i])>1:
								if self.code[i][-1]=="{":
									number+=1
							if self.code[i]=="}":
								number-=1
							if number==0:
								self.cursor=i
								return
							i+=1
					self.cond+=1
				elif line[2]==";":
					if int(self.var[line[1]])<=int(self.var[line[3]]):
						i=self.cursor
						number=0
						while i<len(self.code):
							if len(self.code[i])>1:
								if self.code[i][-1]=="{":
									number+=1
							if self.code[i]=="}":
								number-=1
							if number==0:
								self.cursor=i
								return
							i+=1
					self.cond+=1
		elif line[1:]=="-$":
			if line[0]=="@":
				self.cmd=0
			elif line[0]=="#":
				self.cmd=1
			elif line[0]=="&":
				self.cmd=2
			elif line[0]=="!":
				self.cmd=3
			elif line[0]=="%":
				self.var["&"]=str(ord(input()))
			elif line[0]==":":
				self.var["&"]=input()
			elif line[0]=="/":
				self.cmd=4
			elif line[0]=="*":
				self.cmd=5
			elif line[0]=="§":
				self.cmd=6
			elif line[0]=="µ":
				self.cmd=7
			elif line[0]=="^":
				self.cmd=8
			else:
				self.error=f"[{self.cursor+1}] The Command doesn't exist"
		elif line[-1]=="-":
			if self.cmd==4:
				self.callAdress=self.cursor
				self.cursor=self.fctAdress[line[:-1]]
				self.inFct=True
			elif self.cmd==2:
				if self.var[line[:-1]]=="128":
					print("\n", end="")
				else:
					print(chr(int(self.var[line[:-1]])), end="")
			elif self.cmd==6:
				self.stack.push(self.var[line[:-1]])
			elif self.cmd==7:
				with open(self.home+"out.bdata", "wb+") as f:
					pickle.dump(self.stack, f)
		elif line[-2]=="-":
			if self.cmd==0:
				self.var[line[-1]]=line[:-2]
			elif self.cmd==5:
				self.var[line[-1]]=self.var[line[0]]
			elif self.cmd==8:
				self.var[line[-1]]=self.createObj(self.object[line[:-2]])
		elif line[-1]=="/":
			if self.cmd==2:
				if self.var[line[:-1]]=="128":
					print("\n", end="")
				else:
					print(self.var[line[:-1]], end="")
			elif self.cmd==6:
				self.var[line[:-1]]=self.stack.pop()
		elif line[-2]==".":
			if self.cmd==1:
				try:
					self.var[line[-1]]=int(self.var[line[-1]])+int(line[:-2])
				except:
					self.var[line[-1]]=int(self.var[line[-1]])+int(self.var[line[0]])
			elif self.cmd==8:
				self.stack.push(self.var[line[-1]].get(line[:-2]))
		elif line[-2]==",":
			if self.cmd==1:
				try:
					self.var[line[-1]]=int(self.var[line[-1]])-int(line[:-2])
				except:
					self.var[line[-1]]=int(self.var[line[-1]])-int(self.var[line[0]])
		elif line[-2]==";":
			if self.cmd==1:
				try:
					self.var[line[-1]]=int(self.var[line[-1]])/int(line[:-2])
				except:
					self.var[line[-1]]=int(self.var[line[-1]])/int(self.var[line[0]])
		elif line[-2]==":":
			if self.cmd==1:
				try:
					self.var[line[-1]]=int(self.var[line[-1]])*int(line[:-2])
				except:
					self.var[line[-1]]=int(self.var[line[-1]])*int(self.var[line[0]])
		elif line[-2]=="/":
			if self.cmd==1:
				try:
					self.var[line[-1]]=int(self.var[line[-1]])**int(line[:-2])
				except:
					self.var[line[-1]]=int(self.var[line[-1]])**int(self.var[line[0]])
			elif self.cmd==8:
				self.var[line[-1]].callFunc(line[:-2])
		elif line[-2]=="\\":
			if self.cmd==1:
				try:
					self.var[line[-1]]=int(self.var[line[-1]])%int(line[:-2])
				except:
					self.var[line[-1]]=int(self.var[line[-1]])%int(self.var[line[0]])
		elif line[-1]=="{":
			self.fctAdress[line[:-1]]=self.cursor
			i=self.cursor
			number=0
			while i<len(self.code):
				if len(self.code[i])>1:
					if self.code[i][-1]=="{":
						number+=1
				if self.code[i]=="}":
					number-=1
				if number==0:
					self.cursor=i
					return
				i+=1
		elif line[-1]=="$":
			print("")
			time.sleep(int(self.var[line[:-1]]))
		
	def execute(self):
		while self.cursor<len(self.code):
			try:
				self.interprete(self.code[self.cursor])
				if self.error!=None:
					print(self.error)
					return
				self.cursor+=1
			except Exception as e:
				print(f"An error occured at line {self.cursor+1}: {e}")
				quit()
	
	def createObj(self, data):
		obj=parentObj(self)
		for d in data:
			l=d.split(":")
			if l[1]=="get":
				obj.var[l[0]]=self.stack.pop()
			elif (d:=l[1].split(" "))[0]=="set":
				obj.var[l[0]]=d[1]
			else:
				obj.addFunc(l[0], l[1].replace(" ", ""))
		return obj

	def read(self, path):
		if path[-4:]==".def":
			with open(self.home+path) as f:
				definitions = f.read().split("\n")
			code=""
			if (icl:=definitions[1].split(":")[1])!="":
				include = icl.split(",")
				for el in include:
					with open(self.home+el) as f:
						code+=f.read()+"\n"
			if (obj:=definitions[2].split(":")[1])!="":
				obj = obj.split(",")
				for o in obj:
					with open(self.home+o) as f:
						data=f.read()
						data=[l.strip() for l in data.split("\n")]
						name=data[0][:-1]
						data=data[1:-1]
						self.object[name]=data
			with open(self.home+definitions[0].split(":")[1]) as f:
				code+=f.read()
			self.code = code.split("\n")
			self.code = [line.strip() for line in self.code]
			self.execute()
		elif path[-2:]==".b":
			with open(self.home+path) as f:
				code = f.read()
			self.code = code.split("\n")
			self.code = [line.strip() for line in self.code]
			self.execute()
		elif path[-6:]==".bFunc":
			with open(self.home+path) as f:
				code = f.read()
			self.objFunc=True
			self.code = code.split("\n")
			self.code = [line.strip() for line in self.code]
			self.execute()
		else:
			print("This isn't the good format !")


def main(path, home):
	interpreter = Interpreter(home)
	interpreter.read(path)

if __name__=="__main__":
	file = sys.argv[1]
	if file[0]=="/":
		dct=""
	else:
		dct = os.getcwd()
	file=file.split("/")
	if len(file)==1:
		main(file[0], dct+"/")
	else:
		dct+="/"+"/".join(file[:-1])
		main(file[-1], dct+"/")