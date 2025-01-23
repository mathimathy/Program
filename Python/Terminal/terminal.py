import os
import shutil
import boa as boa
import colorama
class Terminal:
	def __init__(self):
		self.path=os.environ["HOME"]
		self.running=True
		self.b = boa.main
		print("\n"*50)
	def execute(self,cmd):
		cmd=cmd.split(" ")
		if cmd[0]=="clear" or cmd[0]=="cls":
			return "\n"*50
		elif cmd[0]=="mkdir":
			try:
				os.mkdir(self.path+"/"+cmd[1])
				return "The directory has been created"
			except:
				return 'An error occured, the directory hasn\'t been created'
		elif cmd[0]=="rm":
			try:
				os.remove(self.path+"/"+cmd[1])
				return "The file has been deleted"
			except:
				return "An error occured, the file hasn't been deleted"
		elif cmd[0]=="rmdir":
			try:
				os.rmdir(self.path+"/"+cmd[1])
				return "The directory has been deleted"
			except:
				return "An error occured, the directory hasn't been deleted"
		elif cmd[0]=="cd":
			try:
				if cmd[1]=="..":
					path=self.path.split("/")
					path=path[1:-1]
					self.path=""
					for di in path:
						self.path+="/"+di
				else:
					path=""
					for com in cmd[1:]:
						path+=com
						if com!=cmd[-1]:
							path+=" "
					newpath = self.path+"/"+path
					if os.path.isdir(newpath):
						self.path+="/"+path
					else:
						return "This directory doesn't exist"
				
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
				if os.isfile(self.path+"/"+cmd[1]):
					shutil.copyfile(self.path+'\\'+cmd[1], self.path+"/"+cmd[2])
					return "The file has been copied"
				else:
					shutil.copydir(self.path+'\\'+cmd[1], self.path+"/"+cmd[2])
					return "The directory has been copied"
			except:
				return "An error occured, couldn't copy the file/directory"
		elif cmd[0]=="ls" or cmd[0]=="l":
			try:
				listdir =  os.listdir(self.path)
				newlist = ""
				for el in listdir:
					if os.path.isdir(self.path+"/"+el):
						newlist+=colorama.Fore.GREEN+el+colorama.Fore.RESET+"\n"
					else:
						newlist+=el+"\n"
				return newlist
			except:
				return "An error occured, couldn't display the content of the current directory"
		elif cmd[0]=="python":
			try:
				os.system(self.path+"/"+cmd[1])
			except:
				return "An error occured, couldn't run the python file"
		elif cmd[0]=="boa":
			try:
				self.b(cmd[1], self.path+"/")
				return ""
			except:
				return 'An error occured, couldn\'t run the boa file'
		elif cmd[0]=="help":
			return """clear/cls: clear the screen
mkdir <directory>: create a directory
rm <file>: delete a file
rmdir <directory>: delete a directory
cd <directory>: change directory
loc: show current directory location
exit/quit/stop: shutdown the terminal
rename <old> <new>: rename a file or a directory
copy <source> <destination>: copy a file or a directory
ls/l: show current directory content
python <file>: run a python script
boa <file>: run a boa script
help: show help message"""
		else:
			return "This command doesn't exist. Type 'help' to see all the commands"

	def getInput(self):
		cmd=input(colorama.Fore.MAGENTA+colorama.Style.BRIGHT+self.path+colorama.Style.RESET_ALL+"> ")
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