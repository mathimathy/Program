import sqlite3
import nom
import adverbe
import conjonction
import preposition
import adjectif
import demonstratif
import pronom_personnel as pp
import pronom_relatif as pr
import verbe
from colorama import Fore, Style
from colorama import init
def main():
	init()
	txt=input().lower()
	print("\n"*3)
	if txt[-1]==".":
		txt=txt[:-1]
	txt=txt.split(".")
	analyse=[]
	for phrase in txt:
		phrase = phrase.split(",")
		analyse_phrase=[]
		for prop in phrase:
			prop = prop.split(" ")
			analyse_prop={}
			for mot in prop:
				result=[]
				nature=""
				if nom.nom(mot)!=None:
					result = nom.nom(mot)
					nature="nom"
					print(Fore.WHITE + Style.BRIGHT + f"{mot}: {result}" + Style.RESET_ALL)
				elif adverbe.adverbe(mot)!=None and result==[]:
					result = adverbe.adverbe(mot)
					nature="adverbe"
					print(Fore.RED + f"{mot}: {result}" + Fore.RESET)
				
				elif conjonction.conj(mot)!=None and result==[]:
					result = conjonction.conj(mot)
					nature="conjonction"
					print(Fore.GREEN + f"{mot}: {result}" + Fore.RESET)
				
				elif preposition.prep(mot)!=None and result==[]:
					result = preposition.prep(mot)
					nature="preposition"
					print(Fore.YELLOW + f"{mot}: {result}" + Fore.RESET)
				
				elif adjectif.adjectif(mot)!=None and result==[]:
					result = adjectif.adjectif(mot)
					nature="adjectif"
					print(Fore.BLUE + f"{mot}: {result}" + Fore.RESET)
				
				elif adjectif.comparatif(mot)!=None and result==[]:
					result = adjectif.comparatif(mot)
					nature="comparatif"
					print(Fore.BLUE + f"{mot}: {result}" + Fore.RESET)
				
				elif adjectif.superlatif(mot)!=None and result==[]:
					result=adjectif.superlatif(mot)
					nature="superlatif"
					print(Fore.BLUE + f"{mot}: {result}" + Fore.RESET)
				
				elif demonstratif.demonstratif(mot)!=None and result==[]:
					result=demonstratif.demonstratif(mot)
					nature="demonstratif"
					print(Fore.CYAN + f"{mot}: {result}" + Fore.RESET)
				
				elif pp.personel(mot)!=None and result==[]:
					result=pp.personel(mot)
					nature="pronom personnel"
					print(Fore.CYAN + f"{mot}: {result}" + Fore.RESET)
				elif pr.relatif(mot)!=None and result==[]:
					result=pr.relatif(mot)
					nature="pronom relatif"
					print(Fore.CYAN + f"{mot}: {result}" + Fore.RESET)
				
				elif verbe.verbe(mot)!=None and result==[]:
					result=verbe.verbe(mot)
					nature="verbe"
					print(Fore.MAGENTA + f"{mot}: {result}" + Fore.RESET)
				elif verbe.conj_etre(mot)!=None and result==[]:
					result=verbe.conj_etre(mot)
					nature="Verbe Etre"
					print(Fore.MAGENTA + f"{mot}: {result}" + Fore.RESET)
				else:
					print(f'{mot}: {result}')
				analyse_prop[mot]=(nature,result)
			analyse_phrase.append(analyse_prop)
		analyse.append(analyse_phrase)
	# print(analyse)
if __name__=="__main__":
	main()