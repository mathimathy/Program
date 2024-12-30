import math
def main():
	while True:
		result=""
		while True:
			x=input("nombre ")
			if x=="quitter" or x=="q":
				quit()
			try:
				if x.lower()=="ans" or x=='a':
					x=ans
				else:
					x=float(x)
				break
			except:
				print("Attention il faut un nombre !")
		symbol=input("Symbole ")
		if symbol=="quitter" or symbol=="q":
			quit()
		elif symbol not in SINGLE_PARAMETER_OP:
			while True:
				y=input("nombre ")
				if y=="quitter" or y=='q':
					quit()
				try:
					if y=="":
						y=None
					elif y.lower()=="ans" or y=="a":
						y=ans
					else:
						y=float(y)
					break
				except:
					print("Attention il faut un nombre !")

		if symbol=="+":
			result=x+y
		elif symbol=="-":
			result=x-y
		elif symbol=="*":
			result=x*y
		elif symbol=="/":
			if y==0:
				print("Le 2e nombre doit être différent de 0 !")
			else:
				result=x/y
		elif symbol=="%":
			result=x%y
		elif symbol=="sqrt":
			if x<0:
				print("Le nombre doit être positif !")
			else:
				result=math.sqrt(x)
		elif symbol=="exp":
			result=math.exp(x)
		elif symbol=="ln":
			if x<=0:
				print("Le nombre doit être supérieur à 0 !")
			result=math.log(x)
		elif symbol=="!":
			if x<0:
				print("Le nombre doit être positif !")
			else:
				result=math.factorial(x)
		elif symbol=='log':
			if x<=0:
				print("Le nombre doit être supérieur à 0 !")
			else:
				if y==None:
					result=math.log10(x)
				else:
					if y<=0:
						print("La base doit être supérieur à 0 !")
					else:
						result=math.log(x,int(y))
		elif symbol=="**":
			result=x**y
		if result!="":
			print(f"Le résultat est {result}.")
			ans=result
	

if __name__ == '__main__':
	print("\n"*50)
	SINGLE_PARAMETER_OP=["sqrt",'exp',"ln","!"]
	ans=0
	result=""
	main()