import sqlite3

def nom(mot):

	con = sqlite3.Connection('vocLatin.db')

	cur = con.cursor()

	declinaison=[
	["a","a","am","ae","ae","a","ae","ae","as","arum","is","is"],
	["us","e","um","i","o","o","i","i","os","orum","is","is"],
	["","","em","is","i","e","es","es","es","um","ibus","ibus"],
	["us","us","um","us","ui","u","us","us","us","uum","ibus","ibus"],
	["es","es","em","ei","ei","e","es","es","es","erum","ebus","ebus"]
	]
	declinaison_neutre=[
	["er","er","um","i","o","o","i","i","os","orum","is","is"],
	["um","um","um","i","o","o","a","a","a","orum","is","is"],
	["","","","is","i","e","a","a","a","um","ibus","ibus"],
	["","","","is","i","i","ia","ia","ia","ium","ibus","ibus"]]
	posib_1=[]
	posib_2=[]
	posib_2er=[]
	posib_2N=[]
	posib_3=[]
	posib_3N=[]
	posib_3N3I=[]
	posib_4=[]
	posib_5=[]
	decl=declinaison[0]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_1.append(i)
		except:
			pass
		try:
			if mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_1.append(i)
		except:
			pass
		try:
			if mot[-2]+mot[-1]==decl[i]:
				posib_1.append(i)
		except:
			pass
		try:	
			if mot[-1]==decl[i]:
				posib_1.append(i)
		except:
			pass
		i+=1
	decl=declinaison[1]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_2.append(i)
		except:
			pass
		try:
			if mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_2.append(i)
		except:
			pass
		try:
			if mot[-2]+mot[-1]==decl[i]:
				posib_2.append(i)
		except:
			pass
		try:	
			if mot[-1]==decl[i]:
				posib_2.append(i)
		except:
			pass
		i+=1
	decl=declinaison[2]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_3.append(i)
		except:
			pass
		try:
			if mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_3.append(i)
		except:
			pass
		try:
			if mot[-2]+mot[-1]==decl[i]:
				posib_3.append(i)
		except:
			pass
		try:	
			if mot[-1]==decl[i]:
				posib_3.append(i)
		except:
			pass
		i+=1
	decl=declinaison[3]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_4.append(i)
		except:
			pass
		try:
			if mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_4.append(i)
		except:
			pass
		try:
			if mot[-2]+mot[-1]==decl[i]:
				posib_4.append(i)
		except:
			pass
		try:	
			if mot[-1]==decl[i]:
				posib_4.append(i)
		except:
			pass
		i+=1
	decl=declinaison[4]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_5.append(i)
		except:
			pass
		try:
			if mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_5.append(i)
		except:
			pass
		try:
			if mot[-2]+mot[-1]==decl[i]:
				posib_5.append(i)
		except:
			pass
		try:	
			if mot[-1]==decl[i]:
				posib_5.append(i)
		except:
			pass
		i+=1
	decl=declinaison_neutre[0]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_2er.append(i)
		except:
			pass
		try:
			if mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_2er.append(i)
		except:
			pass
		try:
			if mot[-2]+mot[-1]==decl[i]:
				posib_2er.append(i)
		except:
			pass
		try:	
			if mot[-1]==decl[i]:
				posib_2er.append(i)
		except:
			pass
		i+=1
	decl=declinaison_neutre[1]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_2N.append(i)
		except:
			pass
		try:
			if mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_2N.append(i)
		except:
			pass
		try:
			if mot[-2]+mot[-1]==decl[i]:
				posib_2N.append(i)
		except:
			pass
		try:	
			if mot[-1]==decl[i]:
				posib_2N.append(i)
		except:
			pass
		i+=1
	decl=declinaison_neutre[2]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_3N.append(i)
		except:
			pass
		try:
			if mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_3N.append(i)
		except:
			pass
		try:
			if mot[-2]+mot[-1]==decl[i]:
				posib_3N.append(i)
		except:
			pass
		try:	
			if mot[-1]==decl[i]:
				posib_3N.append(i)
		except:
			pass
		i+=1
	decl=declinaison_neutre[3]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_3N3I.append(i)
		except:
			pass
		try:
			if mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_3N3I.append(i)
		except:
			pass
		try:
			if mot[-2]+mot[-1]==decl[i]:
				posib_3N3I.append(i)
		except:
			pass
		try:	
			if mot[-1]==decl[i]:
				posib_3N3I.append(i)
		except:
			pass
		i+=1
	cas=[]
	ligne=[]
	for row in cur.execute("SELECT * FROM nom"):
		if row[3]=="1":
			if 0 in posib_1:
				if mot==row[1]:
					cas.append("NOMINATIF SG")
					cas.append("VOCATIF SG")
					cas.append("ABLATIF SG")
					ligne=row

			elif 9 in posib_1:
				if mot[:-4]+'ae'==row[2]:
					cas.append('GENITIF PL')
					ligne=row
			elif 2 in posib_1:
				if mot[:-2]+'ae'==row[2]:
					cas.append('ACCUSATIF SG')
					ligne=row
			elif 3 in posib_1:
				if mot==row[2]:
					cas.append("GENITIF SG")
					cas.append("DATIF SG")
					cas.append('NOMINATIF PL')
					cas.append('VOCATIF PL')
					ligne=row
			elif 8 in posib_1:
				if mot[:-2]+'ae'==row[2]:
					cas.append('ACCUSATIF PL')
					ligne=row
			elif 10 in posib_1:
				if mot[:-2]+'ae'==row[2]:
					cas.append('DATIF PL')
					cas.append('ABLATIF PL')
					ligne=row
		elif row[3]=="2":
			if 0 in posib_2:
				if mot==row[1]:
					cas.append("NOMINATIF SG")
					ligne=row

			elif 9 in posib_2:
				if mot[:-4]+"i"==row[2]:
					cas.append("GENITIF PL")
					ligne=row
			elif 1 in posib_2:
				if mot[:-1]+"i"==row[2]:
					cas.append("VOCATIF SG")
					ligne=row
			elif 2 in posib_2:
				if mot[:-2]+"i"==row[2]:
					cas.append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_2:
				if mot==row[2]:
					cas.append("GENITIF SG")
					cas.append("NOMINATIF PL")
					cas.append("VOCATIF PL")
					ligne=row
			elif 4 in posib_2:
				if mot[:-1]+"i"==row[2]:
					cas.append("DATIF SG")
					cas.append("ABLATIF SG")
					ligne=row
			elif 8 in posib_2:
				if mot[:-2]+"i"==row[2]:
					cas.append("ACCUSATIF PL")
					ligne=row
			elif 10 in posib_2:
				if mot[:-1]==row[2]:
					cas.append("DATIF PL")
					cas.append("ABLATIF PL")
					ligne=row
		elif row[3]=="2er":
			if 0 in posib_2er:
				if mot==row[1]:
					cas.append("NOMINATIF SG")
					cas.append("VOCATIF SG")
					ligne=row

			elif 9 in posib_2er:
				if mot[:-4]+"i"==row[2]:
					cas.append("GENITIF PL")
					ligne=row
			elif 2 in posib_2er:
				if mot[:-2]+"i"==row[2]:
					cas.append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_2er:
				if mot==row[2]:
					cas.append("GENITIF SG")
					cas.append("NOMINATIF PL")
					cas.append("VOCATIF PL")
					ligne=row
			elif 4 in posib_2er:
				if mot[:-1]+"i"==row[2]:
					cas.append("DATIF SG")
					cas.append("ABLATIF SG")
					ligne=row
			elif 8 in posib_2er:
				if mot[:-2]+"i"==row[2]:
					cas.append("ACCUSATIF PL")
					ligne=row
			elif 10 in posib_2er:
				if mot[:-1]==row[2]:
					cas.append("DATIF PL")
					cas.append("ABLATIF PL")
					ligne=row
		elif row[3]=="2N":
			if 9 in posib_2N:
				if mot[:-4]+"i"==row[2]:
					cas.append("GENITIF PL")
					ligne=row
			elif 0 in posib_2N:
				if mot==row[1]:
					cas.append("NOMINATIF SG")
					cas.append("VOCATIF SG")
					cas.append("ACCUSATIF SG")
					ligne=row

			elif 3 in posib_2N:
				if mot==row[2]:
					cas.append("GENITIF SG")
					ligne=row
			elif 4 in posib_2N:
				if mot[:-1]+"i"==row[2]:
					cas.append("DATIF SG")
					cas.append("ABLATIF SG")
					ligne=row
			elif 6 in posib_2N:
				if mot[:-1]+"i"==row[2]:
					cas.append("NOMINATIF PL")
					cas.append("VOCATIF PL")
					cas.append("ACCUSATIF PL")
					ligne=row
			elif 10 in posib_2N:
				if mot[:-1]==row[2]:
					cas.append("DATIF PL")
					cas.append("ABLATIF PL")
					ligne=row
		elif row[3]=="4":
			if 9 in posib_4:
				if mot[:-3]+"i"==row[2]:
					cas.append("GENITIF PL")
					ligne=row
			elif 10 in posib_4:
				if mot[:-4]+"us"==row[2]:
					cas.append("DATIF PL")
					cas.append("ABLATIF PL")
					ligne=row
			elif 0 in posib_4:
				if mot==row[1]:
					cas.append("NOMINATIF SG")
					cas.append("VOCATIF SG")
					cas.append("GENITIF SG")
					cas.append("NOMINATIF PL")
					cas.append("VOCATIF PL")
					cas.append("ACCUSATIF PL")
					ligne=row
			elif 3 in posib_4:
				if mot[:-1]+"s"==row[2]:
					cas.append("ACCUSATIF SG")
					ligne=row
			elif 4 in posib_4:
				if mot[:-1]+"s"==row[2]:
					cas.append("DATIF SG")
					ligne=row
			elif 5 in posib_4:
				if mot+"s"==row[1]:
					cas.append("ABLATIF SG")
					ligne=row
		elif row[3]=="5":
			if 9 in posib_5:
				if mot[:-4]+"ei"==row[2]:
					cas.append("GENITIF PL")
					ligne=row
			elif 0 in posib_5:
				if mot==row[1]:
					cas.append("NOMINATIF SG")
					cas.append("VOCATIF SG")
					cas.append("NOMINATIF PL")
					cas.append("VOCATIF PL")
					cas.append("ACCUSATIF PL")
					ligne=row
			elif 2 in posib_5:
				if mot[:-1]+'i'==row[2]:
					cas.append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_5:
				if mot==row[2]:
					cas.append("GENITIF SG")
					cas.append("DATIF SG")
					ligne=row
			if 5 in posib_5:
				if mot+"i"==row[2]:
					cas.append("ABLATIF SG")
					ligne=row
			elif 10 in posib_5:
				if mot[:-4]+"ei"==row[2]:
					cas.append("DATIF PL")
					cas.append("ABLATIF PL")
					ligne=row
		elif row[3]=="3":
			if mot==row[1]:
				cas.append("NOMINATIF SG")
				cas.append("VOCATIF SG")
				ligne=row
			if 2 in posib_3:
				if mot[:-2]+"is"==row[2]:
					cas.append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_3:
				if mot==row[2]:
					cas.append("GENITIF SG")
					ligne=row
			elif 4 in posib_3:
				if mot+'s'==row[2]:
					cas.append("DATIF SG")
					ligne=row
			elif 5 in posib_3:
				if mot[:-1]+"is"==row[2]:
					cas.append("ABLATIF SG")
					ligne=row
			elif 6 in posib_3:
				if mot[:-2]+"is"==row[2]:
					cas.append("NOMINATIF PL")
					cas.append("VOCATIF PL")
					cas.append("ACCUSATIF PL")
					ligne=row
			elif 9 in posib_3:
				if mot[:-2]+"is"==row[2] or mot[:-3]+"is"==row[2]:
					cas.append("GENETIF PL")
					ligne=row
			elif 10 in posib_3:
				if mot[:-4]+'is'==row[2]:
					cas.append("DATIF PL")
					cas.append("ABLATIF PL")
					ligne=row
		elif row[3]=="3N":
			if mot==row[1]:
				cas.append("NOMINATIF SG")
				cas.append("VOCATIF SG")
				cas.append("ACCUSATIF SG")
				ligne=row
			if 3 in posib_3N:
				if mot==row[2]:
					cas.append("GENITIF SG")
					ligne=row
			elif 4 in posib_3N:
				if mot+'s'==row[2]:
					cas.append("DATIF SG")
					ligne=row
			elif 5 in posib_3N:
				if mot[:-1]+"is"==row[2]:
					cas.append("ABLATIF SG")
					ligne=row
			elif 6 in posib_3N:
				if mot[:-1]+"is"==row[2]:
					cas.append("NOMINATIF PL")
					cas.append("VOCATIF PL")
					cas.append("ACCUSATIF PL")
					ligne=row
			elif 9 in posib_3N:
				if mot[:-2]+"is"==row[2] or mot[:-3]+"is"==row[2]:
					cas.append("GENETIF PL")
					ligne=row
			elif 10 in posib_3N:
				if mot[:-4]+'is'==row[2]:
					cas.append("DATIF PL")
					cas.append("ABLATIF PL")
					ligne=row
		elif row[3]=="3N3I":
			if mot==row[1]:
				cas.append("NOMINATIF SG")
				cas.append("VOCATIF SG")
				cas.append("ACCUSATIF SG")
				ligne=row
			if 3 in posib_3N3I:
				if mot==row[2]:
					cas.append("GENITIF SG")
					ligne=row
			elif 4 in posib_3N3I:
				if mot+'s'==row[2]:
					cas.append("DATIF SG")
					cas.append("ABLATIF SG")
					ligne=row
			elif 6 in posib_3N3I:
				if mot[:-2]+"is"==row[2]:
					cas.append("NOMINATIF PL")
					cas.append("VOCATIF PL")
					cas.append("ACCUSATIF PL")
					ligne=row
			elif 9 in posib_3N3I:
				if mot[:-3]+"is"==row[2]:
					cas.append("GENETIF PL")
					ligne=row
			elif 10 in posib_3N3I:
				if mot[:-4]+'is'==row[2]:
					cas.append("DATIF PL")
					cas.append("ABLATIF PL")
					ligne=row
	con.close()
	if row==[] or cas==[]:
		return None
	else:		
		return [ligne,cas]