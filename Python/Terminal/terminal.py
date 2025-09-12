import os
import shutil
import boa as boa
import colorama
import platform
class Terminal:
	def __init__(self):
		colorama.init(convert=True)
		if platform.system()=="Windows":
			self.path=os.environ["USERPROFILE"]
			self.separator="\\"
			self.root="C:"
		else:
			self.path=os.environ["HOME"]
			self.separator='/'
			self.root=""
		self.running=True
		self.b = boa.main
		print("\n"*50)
	def execute(self,cmd):
		cmd=cmd.split(" ")
		if cmd[0]=="clear" or cmd[0]=="cls":
			return "\n"*100
		elif cmd[0]=="mkdir":
			try:
				os.mkdir(self.path+self.separator+cmd[1])
				return "The directory has been created"
			except:
				return 'An error occured, the directory hasn\'t been created'
		elif cmd[0]=="rm":
			try:
				os.remove(self.path+self.separator+cmd[1])
				return "The file has been deleted"
			except:
				return "An error occured, the file hasn't been deleted"
		elif cmd[0]=="rmdir":
			try:
				shutil.rmtree(self.path+self.separator+cmd[1])
				return "The directory has been deleted"
			except:
				return "An error occured, the directory hasn't been deleted"
		elif cmd[0]=="cd":
			try:
				if cmd[1]=="..":
					path=self.path.split(self.separator)
					path=path[1:-1]
					self.path=self.root
					for di in path:
						self.path+=self.separator+di
				else:
					path=""
					for com in cmd[1:]:
						path+=com
						if com!=cmd[-1]:
							path+=" "
					newpath = self.path+self.separator+path
					if os.path.isdir(newpath):
						self.path+=self.separator+path
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
			
		elif cmd[0]=="rename" or cmd[0]=="rn":
			try:
				os.rename(self.path+self.separator+cmd[1],self.path+self.separator+cmd[2])
				return "The file/directory has been renamed"
			except:
				return "An error occured, couldn't renamed the file/directory"
		elif cmd[0]=="copy" or cmd[0]=="cp":
			try:
				if os.isfile(self.path+self.separator+cmd[1]):
					shutil.copyfile(self.path+self.separator+cmd[1], self.path+self.separator+cmd[2])
					return "The file has been copied"
				else:
					shutil.copydir(self.path+self.separator+cmd[1], self.path+self.separator+cmd[2])
					return "The directory has been copied"
			except:
				return "An error occured, couldn't copy the file/directory"
		elif cmd[0]=="ls" or cmd[0]=="l" or cmd[0]=="dir":
			try:
				listdir =  os.listdir(self.path)
				newlist = ""
				for el in listdir:
					if os.path.isdir(self.path+self.separator+el):
						newlist+=colorama.Fore.GREEN+el+colorama.Fore.RESET+"\n"
					else:
						newlist+=el+"\n"
				return newlist
			except:
				return "An error occured, couldn't display the content of the current directory"
		elif cmd[0]=="python" or cmd[0]=="py":
			try:
				os.system(self.path+self.separator+cmd[1])
			except:
				return "An error occured, couldn't run the python file"
		elif cmd[0]=="boa":
			try:
				self.b(cmd, self.path)
				return ""
			except:
				return 'An error occured, couldn\'t execute the boa command'
		elif cmd[0]=="chroot":
			try:
				if os.path.isdir(cmd[1]):
					if cmd[1][-1]=='/':
						self.root=cmd[1][:-1]
					else:
						self.root=cmd[1][:-2]
					self.path = cmd[1]
				else:
					return "This directory doesn't exist"
			except:
				return 'An error occured, couldn\'t change the root directory'
		elif cmd[0]=="help":
			return """clear/cls: clear the screen
mkdir <directory>: create a directory
rm <file>: delete a file
rmdir <directory>: delete a directory
cd <directory>: change directory
loc: show current directory location
exit/quit/stop: shutdown the terminal
rename/rn <old> <new>: rename a file or a directory
copy/cp <source> <destination>: copy a file or a directory
ls/l/dir: show current directory content
python/py <file>: run a python script
boa <file>: run a boa script
chroot <dir>: change the root directory to the directory
help: show help message"""
		else:
			return "This command doesn't exist. Type 'help' to see all the commands"
		self.path=self.path.replace("\\\\", '\\').replace("//", "/")

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