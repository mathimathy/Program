import sys
import os
import pickle
import time

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

	def __init__(self, home):
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
		self.stack=Stack()

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
			if self.cmd==5:
				self.var[line[-1]]=self.var[line[0]]
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

	def read(self, path):
		if path[-4:]==".def":
			with open(self.home+path) as f:
				definitions = f.read().split("\n")
			code=""
			include = definitions[1].split(":")[1].split(",")
			for el in include:
				with open(self.home+el) as f:
					code+=f.read()+"\n"
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