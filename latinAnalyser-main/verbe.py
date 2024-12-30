import sqlite3
from sys import exec_prefix
from xml.dom.expatbuilder import parseFragmentString
def verbe(mot):
	ligne=[]
	analyse=[[],[],[],[]]
	term=[
	["o","s","t","mus","tis","nt"],
	["i","isti","it","imus","istis","erunt"],
	["or","ris","tur","mur","mini","ntur"]]
	posib_1=[]
	posib_2=[]
	posib_3=[]
	conj=term[0]
	i=0
	while i<len(conj):
		try:
			if mot[-5]+mot[-4]+mot[-3]+mot[-2]+mot[-1]==conj[i]:
				posib_1.append(i)
		
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==conj[i]:
				posib_1.append(i)
			if mot[-3]+mot[-2]+mot[-1]==conj[i]:
				posib_1.append(i)
			if mot[-2]+mot[-1]==conj[i]:
				posib_1.append(i)
			if mot[-1]==conj[i]:
				posib_1.append(i)
		except:
			pass
		i+=1
	conj=term[1]
	i=0
	while i<len(conj):
		try:
			if mot[-5]+mot[-4]+mot[-3]+mot[-2]+mot[-1]==conj[i]:
				posib_2.append(i)
		
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==conj[i]:
				posib_2.append(i)
			if mot[-3]+mot[-2]+mot[-1]==conj[i]:
				posib_2.append(i)
			if mot[-2]+mot[-1]==conj[i]:
				posib_2.append(i)
			if mot[-1]==conj[i]:
				posib_2.append(i)
		except:
			pass
		i+=1
	if mot[-1]=="m":
		posib_1.append(-1)
	conj=term[2]
	i=0
	while i<len(conj):
		try:
			if mot[-5]+mot[-4]+mot[-3]+mot[-2]+mot[-1]==conj[i]:
				posib_3.append(i)
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==conj[i]:
				posib_3.append(i)
			if mot[-3]+mot[-2]+mot[-1]==conj[i]:
				posib_3.append(i)
			if mot[-2]+mot[-1]==conj[i]:
				posib_3.append(i)
			if mot[-1]==conj[i]:
				posib_3.append(i)
		except:
			pass
		i+=1
	if mot[-1]=="r":
		posib_3.append(-1)
	conn=sqlite3.Connection("vocLatin.db")
	cur=conn.cursor()
	for row in cur.execute("SELECT * FROM verbe"):
		#Indicatif Présent VA
		if row[5]=="1" or row[5]=="2":
			if mot==row[2]:
				analyse[0].append("Indicatif Present")
				analyse[1].append(1)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
			if 1 in posib_1:
				if mot[:-1]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 2 in posib_1:
				if mot[:-1]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 3 in posib_1:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 4 in posib_1:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 5 in posib_1:
				if mot[:-2]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
		if row[5]=="3":
			if mot==row[2]:
				analyse[0].append("Indicatif Present")
				analyse[1].append(1)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
			if 1 in posib_1:
				if mot[:-2]+"ere"==row[1] and mot[-2]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 2 in posib_1:
				if mot[:-2]+"ere"==row[1] and mot[-2]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 3 in posib_1:
				if mot[:-4]+"ere"==row[1] and mot[-2]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 4 in posib_1:
				if mot[:-4]+"ere"==row[1] and mot[-2]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 5 in posib_1:
				if mot[:-3]+"ere"==row[1] and mot[-2]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
		if row[5]=="4":
			if mot==row[2]:
				analyse[0].append("Indicatif Present")
				analyse[1].append(1)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
			if 1 in posib_1:
				if mot[:-1]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 2 in posib_1:
				if mot[:-1]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 3 in posib_1:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 4 in posib_1:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 5 in posib_1:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
		if row[5]=="5":
			if mot==row[2]:
				analyse[0].append("Indicatif Present")
				analyse[1].append(1)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
			if 1 in posib_1:
				if mot[:-2]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 2 in posib_1:
				if mot[:-2]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 3 in posib_1:
				if mot[:-4]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 4 in posib_1:
				if mot[:-4]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 5 in posib_1:
				if mot[:-4]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
		#Indicatif Présent VP
		if row[5]=="1" or row[5]=="2":
			if 0 in posib_3:
				if mot[:-2]+"are"==row[1] or mot[:-1]+"are"==row[1] or mot[:-2]+"re"==row[1] or mot[:-1]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 1 in posib_3:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 2 in posib_3:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 3 in posib_3:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 4 in posib_3:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 5 in posib_3:
				if mot[:-4]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
		if row[5]=="3":
			if 0 in posib_3:
				if mot[:-2]+"ere"==row[1] or mot[:-1]+"ere"==row[1] and mot[-2]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 1 in posib_3:
				if mot[:-4]+"ere"==row[1] and mot[-4]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 2 in posib_3:
				if mot[:-4]+"ere"==row[1] and mot[-4]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 3 in posib_3:
				if mot[:-4]+"ere"==row[1] and mot[-4]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 4 in posib_3:
				if mot[:-4]+"ere"==row[1] and mot[-4]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 5 in posib_3:
				if mot[:-3]+"ere"==row[1] and mot[-3]!="e":
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
		if row[5]=="4":
			if 0 in posib_3:
				if mot[:-2]+"re"==row[1] or mot[:-1]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 1 in posib_3:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 2 in posib_3:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 3 in posib_3:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 4 in posib_3:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 5 in posib_3:
				if mot[:-3]+"re"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
		if row[5]=="5":
			if 0 in posib_3:
				if mot[:-3]+"ere"==row[1] or mot[:-2]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 1 in posib_3:
				if mot[:-4]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 2 in posib_3:
				if mot[:-4]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 3 in posib_3:
				if mot[:-4]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 4 in posib_3:
				if mot[:-4]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 5 in posib_3:
				if mot[:-4]+"ere"==row[1]:
					analyse[0].append("Indicatif Present")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row


		#Indicatif Imparfait VA
		if -1 in posib_1:
			if mot[:-3]+"re"==row[1] and "ba" in mot or mot[:-4]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(1)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
		if 1 in posib_1:
			if mot[:-3]+"re"==row[1] and "ba" in mot or mot[:-4]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(2)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
		if 2 in posib_1:
			if mot[:-3]+"re"==row[1] and "ba" in mot or mot[:-4]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(3)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
		if 3 in posib_1:
			if mot[:-5]+"re"==row[1] and "ba" in mot or mot[:-6]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(1)
				analyse[2].append("PL")
				analyse[3].append("A")
				ligne=row
		if 4 in posib_1:
			if mot[:-5]+"re"==row[1] and "ba" in mot or mot[:-6]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(2)
				analyse[2].append("PL")
				analyse[3].append("A")
				ligne=row
		if 5 in posib_1:
			if mot[:-4]+"re"==row[1] and "ba" in mot or mot[:-5]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(3)
				analyse[2].append("PL")
				analyse[3].append("A")
				ligne=row
		#Indicatif Imparfait VP
		if 0 in posib_3:
			if mot[:-3]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(1)
				analyse[2].append("SG")
				analyse[3].append("P")
				ligne=row
		if 1 in posib_3:
			if mot[:-5]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(2)
				analyse[2].append("SG")
				analyse[3].append("P")
				ligne=row
		if 2 in posib_3:
			if mot[:-5]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(3)
				analyse[2].append("SG")
				analyse[3].append("P")
				ligne=row
		if 3 in posib_3:
			if mot[:-5]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(1)
				analyse[2].append("PL")
				analyse[3].append("P")
				ligne=row
		if 4 in posib_3:
			if mot[:-5]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(2)
				analyse[2].append("PL")
				analyse[3].append("P")
				ligne=row
		if 5 in posib_3:
			if mot[:-4]+"re"==row[1] and "ba" in mot:
				analyse[0].append("Indicatif Imparfait")
				analyse[1].append(3)
				analyse[2].append("PL")
				analyse[3].append("P")
				ligne=row

		#Inficatif Futur Simple VA
		if row[5]=="1" or row[5]=="2":
			if -1 in posib_1:
				if mot[:-3]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(1)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 1 in posib_1:
				if mot[:-3]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 2 in posib_1:
				if mot[:-3]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 3 in posib_1:
				if mot[:-5]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 4 in posib_1:
				if mot[:-5]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 5 in posib_1:
				if mot[:-4]+"re"==row[1] and "bu" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
		else:
			if -1 in posib_1:
				if (mot[:-2]+"ere"==row[1] or mot[:-2]+"re"==row[1]) and "a" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(1)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 1 in posib_1:
				if (mot[:-2]+"ere"==row[1] or mot[:-2]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 2 in posib_1:
				if (mot[:-2]+"ere"==row[1] or mot[:-2]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 3 in posib_1:
				if (mot[:-4]+"ere"==row[1] or mot[:-4]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 4 in posib_1:
				if (mot[:-4]+"ere"==row[1] or mot[:-4]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 5 in posib_1:
				if (mot[:-3]+"ere"==row[1] or mot[:-3]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
		#Inficatif Futur Simple VP
		if row[5]=="1" or row[5]=="2":
			if -1 in posib_3:
				if mot[:-3]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(1)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 1 in posib_3:
				if mot[:-5]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 2 in posib_3:
				if mot[:-5]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("P")
					ligne=row
			if 3 in posib_3:
				if mot[:-5]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 4 in posib_3:
				if mot[:-6]+"re"==row[1] and "bi" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
			if 5 in posib_3:
				if mot[:-6]+"re"==row[1] and "bu" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("P")
					ligne=row
		else:
			if -1 in posib_3:
				if (mot[:-2]+"ere"==row[1] or mot[:-2]+"re"==row[1]) and "a" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(1)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 1 in posib_3:
				if (mot[:-4]+"ere"==row[1] or mot[:-4]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(2)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 2 in posib_3:
				if (mot[:-4]+"ere"==row[1] or mot[:-4]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(3)
					analyse[2].append("SG")
					analyse[3].append("A")
					ligne=row
			if 3 in posib_3:
				if (mot[:-4]+"ere"==row[1] or mot[:-4]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(1)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 4 in posib_3:
				if (mot[:-5]+"ere"==row[1] or mot[:-5]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(2)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row
			if 5 in posib_3:
				if (mot[:-5]+"ere"==row[1] or mot[:-5]+"re"==row[1]) and "e" in mot:
					analyse[0].append("Indicatif Futur Simple")
					analyse[1].append(3)
					analyse[2].append("PL")
					analyse[3].append("A")
					ligne=row


		#Subjonctif Imparfait VA
		if -1 in posib_1:
			if mot[:-1]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(1)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
		if 1 in posib_1:
			if mot[:-1]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(2)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
		if 2 in posib_1:
			if mot[:-1]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(3)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
		if 3 in posib_1:
			if mot[:-3]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(1)
				analyse[2].append("PL")
				analyse[3].append("A")
				ligne=row
		if 4 in posib_1:
			if mot[:-3]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(2)
				analyse[2].append("PL")
				analyse[3].append("A")
				ligne=row
		if 5 in posib_1:
			if mot[:-2]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(3)
				analyse[2].append("PL")
				analyse[3].append("A")
				ligne=row
		#Subjonctif Imparfait VP
		if -1 in posib_3:
			if mot[:-1]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(1)
				analyse[2].append("SG")
				analyse[3].append("P")
				ligne=row
		if 1 in posib_3:
			if mot[:-3]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(2)
				analyse[2].append("SG")
				analyse[3].append("P")
				ligne=row
		if 2 in posib_3:
			if mot[:-3]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(3)
				analyse[2].append("SG")
				analyse[3].append("P")
				ligne=row
		if 3 in posib_3:
			if mot[:-3]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(1)
				analyse[2].append("PL")
				analyse[3].append("P")
				ligne=row
		if 4 in posib_3:
			if mot[:-4]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(2)
				analyse[2].append("PL")
				analyse[3].append("P")
				ligne=row
		if 5 in posib_3:
			if mot[:-4]==row[1]:
				analyse[0].append("Subjonctif Imparfait")
				analyse[1].append(3)
				analyse[2].append("PL")
				analyse[3].append("P")
				ligne=row
		#Infinitif Présent A
		if mot==row[1]:
			analyse[0].append("Infinitif Présent")
			analyse[3].append("A")
			ligne=row
		#Infinitif Present VP
		if row[5]=="1" or row[5]=="2":
			if mot[:-2]+"re"==row[1] and mot[-2:]=="ri":
				analyse[0].append("Infinitif Présent")
				analyse[3].append("P")
				ligne=row
		else:
			if mot[:-1]+"ere"==row[1] and mot[-1:]=="i" or mot[:-1]+"re"==row[1] and mot[-1:]=="i":
				analyse[0].append("Infinitif Présent")
				analyse[3].append("P")
				ligne=row
		#Gerondif
		if mot[-4:]=="ndum" and (mot[:-4]+"re"==row[1] or mot[:-4]+"ere"==row[1]):
			analyse[0].append("Gerondif")
			analyse[3].append("A")
			ligne=row
			analyse[1].append("ACCUSATIF SG")
			analyse[2].append("N")
			analyse[0].append("Adjectif Verbal")
			analyse[3].append("P")
			ligne=row

		if mot[-3:]=="ndi" and (mot[:-3]+"re"==row[1] or mot[:-3]+"ere"==row[1]):
			analyse[0].append("Gerondif")
			analyse[3].append("A")
			ligne=row
			analyse[1].append("GENETIF SG")
			analyse[2].append("N")

		if mot[-3:]=="ndo" and (mot[:-3]+"re"==row[1] or mot[:-3]+"ere"==row[1]):
			analyse[0].append("Gerondif")
			analyse[3].append("A")
			ligne=row
			analyse[1].append("ABLATIF SG")
			analyse[2].append("N")
		#Adjectif Verbale
		if mot[-4:]=="ndus" and (mot[:-4]+"re"==row[1] or mot[:-4]+"ere"==row[1]):
			analyse[0].append("Adjectif Verbal")
			analyse[3].append("P")
			ligne=row
			analyse[2].append("M")
		if mot[-3:]=="nda" and (mot[:-3]+"re"==row[1] or mot[:-3]+"ere"==row[1]):
			analyse[0].append("Adjectif Verbal")
			analyse[3].append("P")
			ligne=row
			analyse[2].append("A")
		#participe present VA
		nomi = row[1][:-2]+"ns"
		geni = row[1][:-2]+"ntis"
		declinaison_2=[
		["","","em","is","i","i","es","es","es","ium","ibus","ibus"],
		["","","","is","i","i","ia","ia","ia","ium","ibus","ibus"]]	
		posib_2MF=[]
		posib_2N=[]
		decl=declinaison_2[0]
		i=0
		while i<len(decl):
			try:

				if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_2MF.append(i)
				if mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_2MF.append(i)
				if mot[-2]+mot[-1]==decl[i]:
					posib_2MF.append(i)
				if mot[-1]==decl[i]:
					posib_2MF.append(i)
			except:
				pass
			i+=1
		decl=declinaison_2[1]
		i=0
		while i<len(decl):
			try:

				if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_2N.append(i)
				if mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_2N.append(i)
				if mot[-2]+mot[-1]==decl[i]:
					posib_2N.append(i)
				if mot[-1]==decl[i]:
					posib_2N.append(i)
			except:
				pass
			i+=1
		if mot==nomi:
			analyse[1].append("NOMINATIF SG")
			analyse[1].append("VOCATIF SG")
			analyse[1].append("NOMINATIF SG")
			analyse[1].append("VOCATIF SG")
			analyse[2].append("F")
			analyse[2].append("M")
			analyse[3].append("A")
			analyse[0].append("Participe Présent")
			ligne=row
		if 2 in posib_2MF:
			if mot[:-2]+"is"==geni:
				analyse[1].append("ACCUSATIF SG")
				analyse[1].append("ACCUSATIF SG")
				analyse[2].append("F")
				analyse[2].append("M")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if 3 in posib_2MF:
			if mot==geni:
				analyse[1].append("GENITIF SG")
				analyse[1].append("GENITIF SG")
				analyse[2].append("F")
				analyse[2].append("M")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if 4 in posib_2MF:
			if mot+'s'==geni:
				analyse[1].append("DATIF SG")
				analyse[1].append("ABLATIF SG")
				analyse[1].append("DATIF SG")
				analyse[1].append("ABLATIF SG")
				analyse[2].append("F")
				analyse[2].append("M")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if 6 in posib_2MF:
			if mot[:-2]+"is"==geni:
				analyse[1].append("NOMINATIF PL")
				analyse[1].append("VOCATIF PL")
				analyse[1].append("ACCUSATIF PL")
				analyse[1].append("NOMINATIF PL")
				analyse[1].append("VOCATIF PL")
				analyse[1].append("ACCUSATIF PL")
				analyse[2].append("F")
				analyse[2].append("M")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if 9 in posib_2MF:
			if mot[:-3]+"is"==geni:
				analyse[1].append("GENETIF PL")
				analyse[1].append("GENETIF PL")
				analyse[2].append("F")
				analyse[2].append("M")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if 10 in posib_2MF:
			if mot[:-4]+'is'==geni:
				analyse[1].append("DATIF PL")
				analyse[1].append("ABLATIF PL")
				analyse[1].append("DATIF PL")
				analyse[1].append("ABLATIF PL")
				analyse[2].append("F")
				analyse[2].append("M")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if mot==nomi:
			analyse[1].append("NOMINATIF SG")
			analyse[1].append("VOCATIF SG")
			analyse[1].append("ACCUSATIF SG")
			analyse[2].append("N")
			analyse[3].append("A")
			analyse[0].append("Participe Présent")
			ligne=row
		if 3 in posib_2N:
			if mot==geni:
				analyse[1].append("GENITIF SG")
				analyse[2].append("N")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if 4 in posib_2N:
			if mot+'s'==geni:
				analyse[1].append("DATIF SG")
				analyse[1].append("ABLATIF SG")
				analyse[2].append("N")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if 6 in posib_2N:
			if mot[:-2]+"is"==geni:
				analyse[1].append("NOMINATIF PL")
				analyse[1].append("VOCATIF PL")
				analyse[1].append("ACCUSATIF PL")
				analyse[2].append("N")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if 9 in posib_2N:
			if mot[:-3]+"is"==geni:
				analyse[1].append("GENETIF PL")
				analyse[2].append("N")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		if 10 in posib_2N:
			if mot[:-4]+'is'==geni:
				analyse[1].append("DATIF PL")
				analyse[1].append("ABLATIF PL")
				analyse[2].append("N")
				analyse[3].append("A")
				analyse[0].append("Participe Présent")
				ligne=row
		#Indicatif Parfait VA
		if 0 in posib_2:
			if mot==row[3]:
				analyse[0].append("Indicatif Parfait")
				analyse[3].append("A")
				analyse[1].append(1)
				analyse[2].append("SG")
				ligne=row
		if 1 in posib_2:
			if mot[:-3]==row[3]:
				analyse[0].append("Indicatif Parfait")
				analyse[3].append("A")
				analyse[1].append(2)
				analyse[2].append("SG")
				ligne=row
		if 2 in posib_2:
			if mot[:-1]==row[3]:
				analyse[0].append("Indicatif Parfait")
				analyse[3].append("A")
				analyse[1].append(3)
				analyse[2].append("SG")
				ligne=row
		if 3 in posib_2:
			if mot[:-3]==row[3]:
				analyse[0].append("Indicatif Parfait")
				analyse[3].append("A")
				analyse[1].append(1)
				analyse[2].append("PL")
				ligne=row
		if 4 in posib_2:
			if mot[:-4]==row[3]:
				analyse[0].append("Indicatif Parfait")
				analyse[3].append("A")
				analyse[1].append(2)
				analyse[2].append("PL")
				ligne=row
		if 5 in posib_2:
			if mot[:-5]+"i"==row[3]:
				analyse[0].append("Indicatif Parfait")
				analyse[3].append("A")
				analyse[1].append(3)
				analyse[2].append("PL")
				ligne=row
		#Inficatif PQP VA
		if -1 in posib_1:
			if mot[-4:-1]=="era" and mot[:-4]+"i"==row[3]:
				analyse[0].append("Indicatif Plus-Que-Parfait")
				analyse[3].append("A")
				analyse[1].append(1)
				analyse[2].append("SG")
				ligne=row
		if 1 in posib_1:
			if mot[-4:-1]=="era" and mot[:-4]+"i"==row[3]:
				analyse[0].append("Indicatif Plus-Que-Parfait")
				analyse[3].append("A")
				analyse[1].append(2)
				analyse[2].append("SG")
				ligne=row
		if 2 in posib_1:
			if mot[-4:-1]=="era" and mot[:-4]+"i"==row[3]:
				analyse[0].append("Indicatif Plus-Que-Parfait")
				analyse[3].append("A")
				analyse[1].append(3)
				analyse[2].append("SG")
				ligne=row
		if 3 in posib_1:
			if mot[-6:-3]=="era" and mot[:-6]+"i"==row[3]:
				analyse[0].append("Indicatif Plus-Que-Parfait")
				analyse[3].append("A")
				analyse[1].append(1)
				analyse[2].append("PL")
				ligne=row
		if 4 in posib_1:
			if mot[-6:-3]=="era" and mot[:-6]+"i"==row[3]:
				analyse[0].append("Indicatif Plus-Que-Parfait")
				analyse[3].append("A")
				analyse[1].append(2)
				analyse[2].append("PL")
				ligne=row
		if 5 in posib_1:
			if mot[-5:-2]=="era" and mot[:-5]+"i"==row[3]:
				analyse[0].append("Indicatif Plus-Que-Parfait")
				analyse[3].append("A")
				analyse[1].append(3)
				analyse[2].append("PL")
				ligne=row
		inf_parf=row[3][:-1]+"isse"
		if mot==inf_parf:
			analyse[0].append("Infinitif Parfait")
			analyse[3].append("A")
			ligne=row
		#Subjonctif PQP VA
		if -1 in posib_1:
			if mot[:-1]==inf_parf:
				analyse[0].append("Subjonctif Plus-Que-Parfait")
				analyse[1].append(1)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
		if 1 in posib_1:
			if mot[:-1]==inf_parf:
				analyse[0].append("Subjonctif Plus-Que-Parfait")
				analyse[1].append(2)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
		if 2 in posib_1:
			if mot[:-1]==inf_parf:
				analyse[0].append("Subjonctif Plus-Que-Parfait")
				analyse[1].append(3)
				analyse[2].append("SG")
				analyse[3].append("A")
				ligne=row
		if 3 in posib_1:
			if mot[:-3]==inf_parf:
				analyse[0].append("Subjonctif Plus-Que-Parfait")
				analyse[1].append(1)
				analyse[2].append("PL")
				analyse[3].append("A")
				ligne=row
		if 4 in posib_1:
			if mot[:-3]==inf_parf:
				analyse[0].append("Subjonctif Plus-Que-Parfait")
				analyse[1].append(2)
				analyse[2].append("PL")
				analyse[3].append("A")
				ligne=row
		if 5 in posib_1:
			if mot[:-2]==inf_parf:
				analyse[0].append("Subjonctif Plus-Que-Parfait")
				analyse[1].append(3)
				analyse[2].append("PL")
				analyse[3].append("A")
				ligne=row
		neutre=row[4]
		masc=row[4][:-1]+"s"
		fem=row[4][:-2]+'a'
		declinaison_1=[
		["us","e","um","i","o","o","i","i","os","orum","is","is"],
		["a","a","am","ae","ae","a","ae","ae","as","arum","is","is"],
		["um","um","um","i","o","o","a","a","a","orum","is","is"]]
		posib_1M=[]
		posib_1F=[]
		posib_1N=[]
		decl=declinaison_1[0]
		i=0
		while i<len(decl):
			try:
				if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_1M.append(i)
				if mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_1M.append(i)
				if mot[-2]+mot[-1]==decl[i]:
					posib_1M.append(i)
				if mot[-1]==decl[i]:
					posib_1M.append(i)
			except:
				pass
			i+=1
		decl=declinaison_1[1]
		i=0
		while i<len(decl):
			try:
				if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_1F.append(i)
				if mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_1F.append(i)
				if mot[-2]+mot[-1]==decl[i]:
					posib_1F.append(i)
				if mot[-1]==decl[i]:
					posib_1F.append(i)
			except:
				pass
			i+=1
		decl=declinaison_1[2]
		i=0
		while i<len(decl):
			try:
				if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_1N.append(i)
				if mot[-3]+mot[-2]+mot[-1]==decl[i]:
					posib_1N.append(i)
				if mot[-2]+mot[-1]==decl[i]:
					posib_1N.append(i)
				if mot[-1]==decl[i]:
					posib_1N.append(i)
			except:
				parseFragmentString
			i+=1
		if 0 in posib_1F:
			if mot==fem:
				analyse[2].append("F")
				analyse[1].append("NOMINATIF SG")
				analyse[1].append("VOCATIF SG")
				analyse[1].append("ABLATIF SG")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 9 in posib_1F:
			if mot[:-4]+'a'==fem:
				analyse[2].append("F")
				analyse[1].append('GENITIF PL')
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 2 in posib_1F:
			if mot[:-2]+'a'==fem:
				analyse[2].append("F")
				analyse[1].append('ACCUSATIF SG')
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 3 in posib_1F:
			if mot[:-1]==fem:
				analyse[2].append("F")
				analyse[1].append("GENITIF SG")
				analyse[1].append("DATIF SG")
				analyse[1].append('NOMINATIF PL')
				analyse[1].append('VOCATIF PL')
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 8 in posib_1F:
			if mot[:-2]+'a'==fem:
				analyse[2].append("F")
				analyse[1].append('ACCUSATIF PL')
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 10 in posib_1F:
			if mot[:-2]+'a'==fem:
				analyse[2].append("F")
				analyse[1].append('DATIF PL')
				analyse[1].append('ABLATIF PL')
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 0 in posib_1M:
			if mot==masc:
				analyse[2].append("M")
				analyse[1].append("NOMINATIF SG")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 9 in posib_1M:
			if mot[:-4]+"us"==masc:
				analyse[2].append("M")
				analyse[1].append("GENITIF PL")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 1 in posib_1M:
			if mot[:-1]+"us"==masc:
				analyse[2].append("M")
				analyse[1].append("VOCATIF SG")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 2 in posib_1M:
			if mot[:-2]+"us"==masc:
				analyse[2].append("M")
				analyse[1].append("ACCUSATIF SG")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 3 in posib_1M:
			if mot[:-1]+"us"==masc:
				analyse[2].append("M")
				analyse[1].append("GENITIF SG")
				analyse[1].append("NOMINATIF PL")
				analyse[1].append("VOCATIF PL")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 4 in posib_1M:
			if mot[:-1]+"us"==masc:
				analyse[2].append("M")
				analyse[1].append("DATIF SG")
				analyse[1].append("ABLATIF SG")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 8 in posib_1M:
			if mot[:-2]+"us"==masc:
				analyse[2].append("M")
				analyse[1].append("ACCUSATIF PL")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 10 in posib_1M:
			if mot[:-2]+"us"==masc:
				analyse[2].append("M")
				analyse[1].append("DATIF PL")
				analyse[1].append("ABLATIF PL")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 9 in posib_1N:
			if mot[:-4]+"um"==neutre:
				analyse[2].append("N")
				analyse[1].append("GENITIF PL")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 0 in posib_1N:
			if mot==neutre:
				analyse[2].append("N")
				analyse[1].append("NOMINATIF SG")
				analyse[1].append("VOCATIF SG")
				analyse[1].append("ACCUSATIF SG")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 3 in posib_1N:
			if mot[:-1]+"um"==neutre:
				analyse[2].append("N")
				analyse[1].append("GENITIF SG")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 4 in posib_1N:
			if mot[:-1]+"um"==neutre:
				analyse[2].append("N")
				analyse[1].append("DATIF SG")
				analyse[1].append("ABLATIF SG")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 6 in posib_1N:
			if mot[:-1]+"um"==neutre:
				analyse[2].append("N")
				analyse[1].append("NOMINATIF PL")
				analyse[1].append("VOCATIF PL")
				analyse[1].append("ACCUSATIF PL")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		if 10 in posib_1N:
			if mot[:-2]+"um"==neutre:
				analyse[1].append("N")
				analyse[1].append("DATIF PL")
				analyse[1].append("ABLATIF PL")
				ligne=row
				analyse[3].append("A")
				analyse[0].append("Participe Parfait")
		
	if ligne==[] and analyse==[[],[],[],[]]:
		return None
	else:
		return [ligne,analyse]

def conj_etre(mot):
	analyse=[[],[],[],["A"]]
	ligne=["esse","sum","fui","","être"]
	if mot=="esse":
		analyse[0].append("Infinitif Present")
	if mot=="fuisse":
		analyse[0].append("Infinitif Parfait")
	if mot=="sum":
		analyse[0].append("Indicatif Present")
		analyse[1].append(1)
		analyse[2].append("SG")
	if mot=="es":
		analyse[0].append("Indicatif Present")
		analyse[1].append(2)
		analyse[2].append("SG")
	if mot=="est":
		analyse[0].append("Indicatif Present")
		analyse[1].append(3)
		analyse[2].append("SG")
	if mot=="sumus":
		analyse[0].append("Indicatif Present")
		analyse[1].append(1)
		analyse[2].append("PL")
	if mot=="estis":
		analyse[0].append("Indicatif Present")
		analyse[1].append(2)
		analyse[2].append("PL")
	if mot=="sunt":
		analyse[0].append("Indicatif Present")
		analyse[1].append(3)
		analyse[2].append("PL")
		
	if mot=="eram":
		analyse[0].append("Indicatif Imparfait")
		analyse[1].append(1)
		analyse[2].append("SG")
	if mot=="eras":
		analyse[0].append("Indicatif Imparfait")
		analyse[1].append(2)
		analyse[2].append("SG")
	if mot=="erat":
		analyse[0].append("Indicatif Imparfait")
		analyse[1].append(3)
		analyse[2].append("SG")
	if mot=="eramus":
		analyse[0].append("Indicatif Imparfait")
		analyse[1].append(1)
		analyse[2].append("PL")
	if mot=="eratis":
		analyse[0].append("Indicatif Imparfait")
		analyse[1].append(2)
		analyse[2].append("PL")
	if mot=="erant":
		analyse[0].append("Indicatif Imparfait")
		analyse[1].append(3)
		analyse[2].append("PL")
		
	if mot=="ero":
		analyse[0].append("Indicatif Futur")
		analyse[1].append(1)
		analyse[2].append("SG")
	if mot=="eris":
		analyse[0].append("Indicatif Futur")
		analyse[1].append(2)
		analyse[2].append("SG")
	if mot=="erit":
		analyse[0].append("Indicatif Futur")
		analyse[1].append(3)
		analyse[2].append("SG")
	if mot=="erimus":
		analyse[0].append("Indicatif Futur")
		analyse[1].append(1)
		analyse[2].append("PL")
	if mot=="eritis":
		analyse[0].append("Indicatif Futur")
		analyse[1].append(2)
		analyse[2].append("PL")
	if mot=="erunt":
		analyse[0].append("Indicatif Futur")
		analyse[1].append(3)
		analyse[2].append("PL")
		
	if mot=="fui":
		analyse[0].append("Indicatif Parfait")
		analyse[1].append(1)
		analyse[2].append("SG")
	if mot=="fuisti":
		analyse[0].append("Indicatif Parfait")
		analyse[1].append(2)
		analyse[2].append("SG")
	if mot=="fuit":
		analyse[0].append("Indicatif Parfait")
		analyse[1].append(3)
		analyse[2].append("SG")
	if mot=="fuimus":
		analyse[0].append("Indicatif Parfait")
		analyse[1].append(1)
		analyse[2].append("PL")
	if mot=="fuistis":
		analyse[0].append("Indicatif Parfait")
		analyse[1].append(2)
		analyse[2].append("PL")
	if mot=="fuerunt":
		analyse[0].append("Indicatif Parfait")
		analyse[1].append(3)
		analyse[2].append("PL")
		
	if mot=="fueram":
		analyse[0].append("Indicatif Plus-Que-Parfait")
		analyse[1].append(1)
		analyse[2].append("SG")
	if mot=="fueras":
		analyse[0].append("Indicatif Plus-Que-Parfait")
		analyse[1].append(2)
		analyse[2].append("SG")
	if mot=="fuerat":
		analyse[0].append("Indicatif Plus-Que-Parfait")
		analyse[1].append(3)
		analyse[2].append("SG")
	if mot=="fueramus":
		analyse[0].append("Indicatif Plus-Que-Parfait")
		analyse[1].append(1)
		analyse[2].append("PL")
	if mot=="fueratis":
		analyse[0].append("Indicatif Plus-Que-Parfait")
		analyse[1].append(2)
		analyse[2].append("PL")
	if mot=="fuerant":
		analyse[0].append("Indicatif Plus-Que-Parfait")
		analyse[1].append(3)
		analyse[2].append("PL")
		
	if mot=="essem":
		analyse[0].append("Subjonctif Imparfait")
		analyse[1].append(1)
		analyse[2].append("SG")
	if mot=="esses":
		analyse[0].append("Subjonctif Imparfait")
		analyse[1].append(2)
		analyse[2].append("SG")
	if mot=="esset":
		analyse[0].append("Subjonctif Imparfait")
		analyse[1].append(3)
		analyse[2].append("SG")
	if mot=="essemus":
		analyse[0].append("Subjonctif Imparfait")
		analyse[1].append(1)
		analyse[2].append("PL")
	if mot=="essetis":
		analyse[0].append("Subjonctif Imparfait")
		analyse[1].append(2)
		analyse[2].append("PL")
	if mot=="essent":
		analyse[0].append("Subjonctif Imparfait")
		analyse[1].append(3)
		analyse[2].append("PL")
		
	if mot=="fuissem":
		analyse[0].append("Subjonctif Plus-Que-Parfait")
		analyse[1].append(1)
		analyse[2].append("SG")
	if mot=="fuisses":
		analyse[0].append("Subjonctif Plus-Que-Parfait")
		analyse[1].append(2)
		analyse[2].append("SG")
	if mot=="fuisset":
		analyse[0].append("Subjonctif Plus-Que-Parfait")
		analyse[1].append(3)
		analyse[2].append("SG")
	if mot=="fuissemus":
		analyse[0].append("Subjonctif Plus-Que-Parfait")
		analyse[1].append(1)
		analyse[2].append("PL")
	if mot=="fuissetis":
		analyse[0].append("Subjonctif Plus-Que-Parfait")
		analyse[1].append(2)
		analyse[2].append("PL")
	if mot=="fuissent":
		analyse[0].append("Subjonctif Plus-Que-Parfait")
		analyse[1].append(3)
		analyse[2].append("PL")
	if analyse==[[],[],[],['A']]:
		return None
	else:
		return [ligne,analyse]