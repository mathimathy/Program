import os
import shutil
import boa
class Terminal:
	def __init__(self):
		self.path=os.environ["HOMEPATH"]
		self.running=True
		self.b = boa.main
		print("\n"*50)
	def execute(self,cmd):
		cmd=cmd.split(" ")
		if cmd[0]=="clear" or cmd[0]=="cls":
			return "\n"*50
		elif cmd[0]=="mkdir":
			try:
				os.mkdir(self.path+"\\"+cmd[1])
				return "The directory has been created"
			except:
				return 'An error occured, the directory hasn\'t been created'
		elif cmd[0]=="rm":
			try:
				os.remove(self.path+"\\"+cmd[1])
				return "The file has been deleted"
			except:
				return "An error occured, the file hasn't been deleted"
		elif cmd[0]=="rmdir":
			try:
				os.rmdir(self.path+"\\"+cmd[1])
				return "The directory has been deleted"
			except:
				return "An error occured, the directory hasn't been deleted"
		elif cmd[0]=="cd":
			try:
				if cmd[1]=="..":
					path=self.path.split("\\")
					path=path[1:-1]
					self.path=""
					for di in path:
						self.path+="\\"+di
				else:
					path=""
					for com in cmd[1:]:
						path+=com
						if com!=cmd[-1]:
							path+=" "
					self.path+="\\"+path
				
			except:
				return "An error occured"
		elif cmd[0]=="loc":
			try:
				return self.path
			except:
				return "An error occured, couldn't show your location"
		elif cmd[0]=="exit" or cmd[0]=="quit" or cmd[0]=="stop":
			self.running=False
			
		elif cmd[0]=="rename":
			try:
				os.rename(self.path+'\\'+cmd[1],self.path+'\\'+cmd[2])
				return "The file/directory has been renamed"
			except:
				return "An error occured, couldn't renamed the file/directory"
		elif cmd[0]=="copy":
			try:
				if os.isfile(self.path+"\\"+cmd[1]):
					shutil.copyfile(self.path+'\\'+cmd[1], self.path+"\\"+cmd[2])
					return "The file has been copied"
				else:
					shutil.copydir(self.path+'\\'+cmd[1], self.path+"\\"+cmd[2])
					return "The directory has been copied"
			except:
				return "An error occured, couldn't copy the file/directory"
		elif cmd[0]=="ls":
			try:
				return os.listdir(self.path)
			except:
				return "An error occured, couldn't display the content of the current directory"
		elif cmd[0]=="python":
			try:
				os.system(self.path+"\\"+cmd[1])
				
			except:
				return "An error occured, couldn't run the python file"
		elif cmd[0]=="boa":
			try:
				self.b(self.path+"\\"+cmd[1])
				return ""
			except:
				return 'An error occured, couldn\'t run the boa file'
		else:
			return "This command doesn't exist"

	def getInput(self):
		cmd=input("> ")
		msg = self.execute(cmd)
		if isinstance(msg, str):
			print(msg)
		elif msg==None:
			pass
		else:
			for i in msg:
				print(i)
		if self.running:
			self.getInput()