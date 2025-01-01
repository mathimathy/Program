def main():
	while True:
		while True:
			try:
				x=int(input("nombre "))
				break
			except:
				print("Attention il faut un nombre !")
		symbole=input("Symbole ")
		while True:
			try:
				y=int(input("nombre "))
				break
			except:
				print("Attention il faut un nombre !")

		if symbole=="+":
			print(f"Le résultat est {x+y}.")
		elif symbole=="-":
			print(f"Le résultat est {x-y}.")
		elif symbole=="*":
			print(f"Le résultat est {x*y}.")
		elif symbole=="/":
			print(f"Le résultat est {x/y}.")
		elif symbole=="quitter":
			quit()
	

if __name__ == '__main__':
	print("\n"*50)
	main()