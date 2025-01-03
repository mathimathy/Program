class Interpreter:

	def __init__(self):
		self.cmd=None
		self.jmpPt=[]
		self.error=None
		self.var={}
		self.cursor=0
		self.code=None
		self.fctAdress={}
		self.inFct=False
		self.callAdress=None

	def interprete(self, line):
		if line=="/":
			if len(self.jmpPt)==1 or len(self.jmpPt)==0:
				self.cursor=len(self.code)
			else:
				del self.jmpPt[-1]
		elif line=="":
			pass
		elif line=="}":
			if self.inFct:
				self.cursor=self.callAdress
				self.inFct=False
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
			else:
				self.error=f"[{self.cursor+1}] The Command doesn't exist"
		elif line[-2]=="-":
			if self.cmd==0:
				self.var[line[-1]]=line[:-2]
			if self.cmd==5:
				self.var[line[-1]]=self.var[line[0]]
		elif line[-1]=="-":
			if self.cmd==4:
				self.callAdress=self.cursor
				self.cursor=self.fctAdress[line[0]]
				self.inFct=True
			if self.cmd==2:
				if self.var[line[:-1]]=="128":
					print("\n", end="")
				else:
					print(chr(int(self.var[line[:-1]])), end="")
		elif line[-1]=="/":
			if self.cmd==2:
				if self.var[line[:-1]]=="128":
					print("\n", end="")
				else:
					print(self.var[line[:-1]], end="")
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
		elif line[:2]=="//":
			pass
		
	def execute(self):
		while self.cursor<len(self.code):
			self.interprete(self.code[self.cursor])
			if self.error!=None:
				print(self.error)
				return
			# print(self.cursor)
			self.cursor+=1

	def read(self, path):
		if path[-2:]==".b":
			f = open(path)
			code = f.read()
			self.code = code.split("\n")
			self.execute()
		else:
			print("This isn't the good format !")


def main(path):
	interpreter = Interpreter()
	interpreter.read(path)