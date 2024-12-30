import sqlite3

def adjectif(mot):
	declinaison_1=[
	["us","e","um","i","o","o","i","i","os","orum","is","is"],
	["a","a","am","ae","ae","a","ae","ae","as","arum","is","is"],
	["um","um","um","i","o","o","a","a","a","orum","is","is"]]
	declinaison_1er=[
	["er","er","um","i","o","o","i","i","os","orum","is","is"]]
	declinaison_2=[
	["","","em","is","i","i","es","es","es","ium","ibus","ibus"],
	["","","","is","i","i","ia","ia","ia","ium","ibus","ibus"]]
	analyse=[[],[],[]]
	ligne=[]
	conn = sqlite3.Connection('vocLatin.db')
	cur = conn.cursor()
	posib_1M=[]
	posib_1F=[]
	posib_1N=[]
	posib_1Mer=[]
	posib_2MF=[]
	posib_2N=[]
	decl=declinaison_1[0]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_1M.append(i)
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_1M.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_1M.append(i)
			elif mot[-1]==decl[i]:
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
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_1F.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_1F.append(i)
			elif mot[-1]==decl[i]:
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
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_1N.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_1N.append(i)
			elif mot[-1]==decl[i]:
				posib_1N.append(i)
		except:
			pass
		i+=1
	decl=declinaison_1er[0]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_1Mer.append(i)
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_1Mer.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_1Mer.append(i)
			elif mot[-1]==decl[i]:
				posib_1Mer.append(i)
		except:
			pass
		i+=1
	decl=declinaison_2[0]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_2MF.append(i)
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_2MF.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_2MF.append(i)
			elif mot[-1]==decl[i]:
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
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_2N.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_2N.append(i)
			elif mot[-1]==decl[i]:
				posib_2N.append(i)
		except:
			pass
		i+=1
	for row in cur.execute("SELECT * FROM adjectif"):
		if row[6]=="1":
			if 0 in posib_1F:
				if mot==row[2]:
					analyse[1].append("NOMINATIF SG")
					analyse[1].append("VOCATIF SG")
					analyse[1].append("ABLATIF SG")
					ligne=row
			elif 9 in posib_1F:
				if mot[:-4]+'a'==row[2]:
					analyse[1].append('GENITIF PL')
					ligne=row
			elif 2 in posib_1F:
				if mot[:-2]+'a'==row[2]:
					analyse[1].append('ACCUSATIF SG')
					ligne=row
			elif 3 in posib_1F:
				if mot[:-1]==row[2]:
					analyse[1].append("GENITIF SG")
					analyse[1].append("DATIF SG")
					analyse[1].append('NOMINATIF PL')
					analyse[1].append('VOCATIF PL')
					ligne=row
			elif 8 in posib_1F:
				if mot[:-2]+'a'==row[2]:
					analyse[1].append('ACCUSATIF PL')
					ligne=row
			elif 10 in posib_1F:
				if mot[:-2]+'a'==row[2]:
					analyse[1].append('DATIF PL')
					analyse[1].append('ABLATIF PL')
					ligne=row
			if 0 in posib_1M:
				if mot==row[1]:
					analyse[0].append("NOMINATIF SG")
					ligne=row
			elif 9 in posib_1M:
				if mot[:-4]+"us"==row[1]:
					analyse[0].append("GENITIF PL")
					ligne=row
			elif 1 in posib_1M:
				if mot[:-1]+"us"==row[1]:
					analyse[0].append("VOCATIF SG")
					ligne=row
			elif 2 in posib_1M:
				if mot[:-2]+"us"==row[1]:
					analyse[0].append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_1M:
				if mot[:-1]+"us"==row[1]:
					analyse[0].append("GENITIF SG")
					analyse[0].append("NOMINATIF PL")
					analyse[0].append("VOCATIF PL")
					ligne=row
			elif 4 in posib_1M:
				if mot[:-1]+"us"==row[1]:
					analyse[0].append("DATIF SG")
					analyse[0].append("ABLATIF SG")
					ligne=row
			elif 8 in posib_1M:
				if mot[:-2]+"us"==row[1]:
					analyse[0].append("ACCUSATIF PL")
					ligne=row
			elif 10 in posib_1M:
				if mot[:-2]+"us"==row[1]:
					analyse[0].append("DATIF PL")
					analyse[0].append("ABLATIF PL")
					ligne=row
			if 9 in posib_1N:
				if mot[:-4]+"um"==row[3]:
					analyse[2].append("GENITIF PL")
					ligne=row
			elif 0 in posib_1N:
				if mot==row[3]:
					analyse[2].append("NOMINATIF SG")
					analyse[2].append("VOCATIF SG")
					analyse[2].append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_1N:
				if mot[:-1]+"um"==row[3]:
					analyse[2].append("GENITIF SG")
					ligne=row
			elif 4 in posib_1N:
				if mot[:-1]+"um"==row[3]:
					analyse[2].append("DATIF SG")
					analyse[2].append("ABLATIF SG")
					ligne=row
			elif 6 in posib_1N:
				if mot[:-1]+"um"==row[3]:
					analyse[2].append("NOMINATIF PL")
					analyse[2].append("VOCATIF PL")
					analyse[2].append("ACCUSATIF PL")
					ligne=row
			elif 10 in posib_1N:
				if mot[:-2]+"um"==row[3]:
					analyse[2].append("DATIF PL")
					analyse[2].append("ABLATIF PL")
					ligne=row
		elif row[6]=="1er":
			if 0 in posib_1F:
				if mot==row[2]:
					analyse[1].append("NOMINATIF SG")
					analyse[1].append("VOCATIF SG")
					analyse[1].append("ABLATIF SG")
					ligne=row
			elif 9 in posib_1F:
				if mot[:-4]+'a'==row[2]:
					analyse[1].append('GENITIF PL')
					ligne=row
			elif 2 in posib_1F:
				if mot[:-2]+'a'==row[2]:
					analyse[1].append('ACCUSATIF SG')
					ligne=row
			elif 3 in posib_1F:
				if mot[:-1]==row[2]:
					analyse[1].append("GENITIF SG")
					analyse[1].append("DATIF SG")
					analyse[1].append('NOMINATIF PL')
					analyse[1].append('VOCATIF PL')
					ligne=row
			elif 8 in posib_1F:
				if mot[:-2]+'a'==row[2]:
					analyse[1].append('ACCUSATIF PL')
					ligne=row
			elif 10 in posib_1F:
				if mot[:-2]+'a'==row[2]:
					analyse[1].append('DATIF PL')
					analyse[1].append('ABLATIF PL')
					ligne=row
			if 0 in posib_1Mer:
				if mot==row[1]:
					analyse[0].append("NOMINATIF SG")
					analyse[0].append("VOCATIF SG")
					ligne=row
			elif 9 in posib_1Mer:
				if mot[:-5]+"er"==row[1]:
					analyse[0].append("GENITIF PL")
					ligne=row
			elif 2 in posib_1Mer:
				if mot[:-3]+"er"==row[1]:
					analyse[0].append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_1Mer:
				if mot[:-2]+"er"==row[1]:
					analyse[0].append("GENITIF SG")
					analyse[0].append("NOMINATIF PL")
					analyse[0].append("VOCATIF PL")
					ligne=row
			elif 4 in posib_1Mer:
				if mot[:-2]+"er"==row[1]:
					analyse[0].append("DATIF SG")
					analyse[0].append("ABLATIF SG")
					ligne=row
			elif 8 in posib_1Mer:
				if mot[:-3]+"er"==row[1]:
					analyse[0].append("ACCUSATIF PL")
					ligne=row
			elif 10 in posib_1Mer:
				if mot[:-3]+"er"==row[1]:
					analyse[0].append("DATIF PL")
					analyse[0].append("ABLATIF PL")
					ligne=row
			if 9 in posib_1N:
				if mot[:-4]+"um"==row[3]:
					analyse[2].append("GENITIF PL")
					ligne=row
			elif 0 in posib_1N:
				if mot==row[3]:
					analyse[2].append("NOMINATIF SG")
					analyse[2].append("VOCATIF SG")
					analyse[2].append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_1N:
				if mot[:-1]+"um"==row[3]:
					analyse[2].append("GENITIF SG")
					ligne=row
			elif 4 in posib_1N:
				if mot[:-1]+"um"==row[3]:
					analyse[2].append("DATIF SG")
					analyse[2].append("ABLATIF SG")
					ligne=row
			elif 6 in posib_1N:
				if mot[:-1]+"um"==row[3]:
					analyse[2].append("NOMINATIF PL")
					analyse[2].append("VOCATIF PL")
					analyse[2].append("ACCUSATIF PL")
					ligne=row
			elif 10 in posib_1N:
				if mot[:-2]+"um"==row[3]:
					analyse[2].append("DATIF PL")
					analyse[2].append("ABLATIF PL")
					ligne=row
		elif row[6]=="2er":
			if mot==row[1]:
				analyse[0].append("NOMINATIF SG")
				analyse[0].append("VOCAITF SG")
				ligne=row
			if mot==row[2]:
				analyse[1].append("NOMINATIF SG")
				analyse[1].append("VOCAITF SG")
				ligne=row
			if 2 in posib_2MF:
				if mot[:-2]==row[1] or mot[:-3]+"er"==row[1]:
					analyse[0].append("ACCUSATIF SG")
					analyse[1].append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_2MF:
				if mot[:-2]==row[1] or mot[:-3]+"er"==row[1]:
					analyse[0].append("GENITIF SG")
					analyse[1].append("GENITIF SG")
					ligne=row
			elif 4 in posib_2MF:
				if mot[:-1]==row[1] or mot[:-2]+"er"==row[1]:
					analyse[0].append("DATIF SG")
					analyse[0].append("ABLATIF SG")
					analyse[1].append("DATIF SG")
					analyse[1].append("ABLATIF SG")
					ligne=row
			elif 6 in posib_2MF:
				if mot[:-2]==row[1] or mot[:-3]+"er"==row[1]:
					analyse[0].append("NOMINATIF PL")
					analyse[0].append("VOCATIF PL")
					analyse[0].append("ACCUSATIF PL")
					analyse[1].append("NOMINATIF PL")
					analyse[1].append("VOCATIF PL")
					analyse[1].append("ACCUSATIF PL")
					ligne=row
			elif 9 in posib_2MF:
				if mot[:-3]==row[1] or mot[:-4]+"er"==row[1]:
					analyse[0].append("GENETIF PL")
					analyse[1].append("GENETIF PL")
					ligne=row
			elif 10 in posib_2MF:
				if mot[:-4]==row[2] or mot[:-5]+"er"==row[1]:
					analyse[0].append("DATIF PL")
					analyse[0].append("ABLATIF PL")
					analyse[1].append("DATIF PL")
					analyse[1].append("ABLATIF PL")
					ligne=row
			if mot==row[3]:
				analyse[2].append("NOMINATIF SG")
				analyse[2].append("VOCATIF SG")
				analyse[2].append("ACCUSATIF SG")
				ligne=row
			if 3 in posib_2N:
				if mot[:-2]+"e"==row[3]:
					analyse[2].append("GENITIF SG")
					ligne=row
			elif 4 in posib_2N:
				if mot[:-1]+"e"==row[3]:
					analyse[2].append("DATIF SG")
					analyse[2].append("ABLATIF SG")
					ligne=row
			elif 6 in posib_2N:
				if mot[:-2]+"e"==row[3]:
					analyse[2].append("NOMINATIF PL")
					analyse[2].append("VOCATIF PL")
					analyse[2].append("ACCUSATIF PL")
					ligne=row
			elif 9 in posib_2N:
				if mot[:-3]+"e"==row[3]:
					analyse[2].append("GENETIF PL")
					ligne=row
			elif 10 in posib_2N:
				if mot[:-4]+'e'==row[3]:
					analyse[2].append("DATIF PL")
					analyse[2].append("ABLATIF PL")
					ligne=row
		elif row[6]=="2.1":
			if mot==row[1]:
				analyse[0].append("NOMINATIF SG")
				analyse[0].append("VOCAITF SG")
				analyse[1].append("NOMINATIF SG")
				analyse[1].append("VOCAITF SG")
				ligne=row
			if 2 in posib_2MF:
				if mot[:-2]+"is"==row[1]:
					analyse[0].append("ACCUSATIF SG")
					analyse[1].append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_2MF:
				if mot[:-2]+"is"==row[1]:
					analyse[0].append("GENITIF SG")
					analyse[1].append("GENITIF SG")
					ligne=row
			elif 4 in posib_2MF:
				if mot[:-1]+"is"==row[1]:
					analyse[0].append("DATIF SG")
					analyse[0].append("ABLATIF SG")
					analyse[1].append("DATIF SG")
					analyse[1].append("ABLATIF SG")
					ligne=row
			elif 6 in posib_2MF:
				if mot[:-2]+"is"==row[1]:
					analyse[0].append("NOMINATIF PL")
					analyse[0].append("VOCATIF PL")
					analyse[0].append("ACCUSATIF PL")
					analyse[1].append("NOMINATIF PL")
					analyse[1].append("VOCATIF PL")
					analyse[1].append("ACCUSATIF PL")
					ligne=row
			elif 9 in posib_2MF:
				if mot[:-3]+"is"==row[1]:
					analyse[0].append("GENETIF PL")
					analyse[1].append("GENETIF PL")
					ligne=row
			elif 10 in posib_2MF:
				if mot[:-4]+"is"==row[2]:
					analyse[0].append("DATIF PL")
					analyse[0].append("ABLATIF PL")
					analyse[1].append("DATIF PL")
					analyse[1].append("ABLATIF PL")
					ligne=row
			if mot==row[3]:
				analyse[2].append("NOMINATIF SG")
				analyse[2].append("VOCATIF SG")
				analyse[2].append("ACCUSATIF SG")
				ligne=row
			if 3 in posib_2N:
				if mot[:-2]+"e"==row[3]:
					analyse[2].append("GENITIF SG")
					ligne=row
			elif 4 in posib_2N:
				if mot[:-1]+"e"==row[3]:
					analyse[2].append("DATIF SG")
					analyse[2].append("ABLATIF SG")
					ligne=row
			elif 6 in posib_2N:
				if mot[:-2]+"e"==row[3]:
					analyse[2].append("NOMINATIF PL")
					analyse[2].append("VOCATIF PL")
					analyse[2].append("ACCUSATIF PL")
					ligne=row
			elif 9 in posib_2N:
				if mot[:-3]+"e"==row[3]:
					analyse[2].append("GENETIF PL")
					ligne=row
			elif 10 in posib_2N:
				if mot[:-4]+'e'==row[3]:
					analyse[2].append("DATIF PL")
					analyse[2].append("ABLATIF PL")
					ligne=row
		elif row[6]=="2.2":
			if mot==row[1]:
				analyse[0].append("NOMINATIF SG")
				analyse[0].append("VOCATIF SG")
				analyse[1].append("NOMINATIF SG")
				analyse[1].append("VOCATIF SG")
				ligne=row
			if 2 in posib_2MF:
				if mot[:-2]+"is"==row[2]:
					analyse[0].append("ACCUSATIF SG")
					analyse[1].append("ACCUSATIF SG")
					ligne=row
			elif 3 in posib_2MF:
				if mot==row[2]:
					analyse[0].append("GENITIF SG")
					analyse[1].append("GENITIF SG")
					ligne=row
			elif 4 in posib_2MF:
				if mot+'s'==row[2]:
					analyse[0].append("DATIF SG")
					analyse[0].append("ABLATIF SG")
					analyse[1].append("DATIF SG")
					analyse[1].append("ABLATIF SG")
					ligne=row
			elif 6 in posib_2MF:
				if mot[:-2]+"is"==row[2]:
					analyse[0].append("NOMINATIF PL")
					analyse[0].append("VOCATIF PL")
					analyse[0].append("ACCUSATIF PL")
					analyse[1].append("NOMINATIF PL")
					analyse[1].append("VOCATIF PL")
					analyse[1].append("ACCUSATIF PL")
					ligne=row
			elif 9 in posib_2MF:
				if mot[:-3]+"is"==row[2]:
					analyse[0].append("GENETIF PL")
					analyse[1].append("GENETIF PL")
					ligne=row
			elif 10 in posib_2MF:
				if mot[:-4]+'is'==row[2]:
					analyse[0].append("DATIF PL")
					analyse[0].append("ABLATIF PL")
					analyse[1].append("DATIF PL")
					analyse[1].append("ABLATIF PL")
					ligne=row
			if mot==row[1]:
				analyse[2].append("NOMINATIF SG")
				analyse[2].append("VOCATIF SG")
				analyse[2].append("ACCUSATIF SG")
				ligne=row
			if 3 in posib_2N:
				if mot==row[2]:
					analyse[2].append("GENITIF SG")
					ligne=row
			elif 4 in posib_2N:
				if mot+'s'==row[2]:
					analyse[2].append("DATIF SG")
					analyse[2].append("ABLATIF SG")
					ligne=row
			elif 6 in posib_2N:
				if mot[:-2]+"is"==row[2]:
					analyse[2].append("NOMINATIF PL")
					analyse[2].append("VOCATIF PL")
					analyse[2].append("ACCUSATIF PL")
					ligne=row
			elif 9 in posib_2N:
				if mot[:-3]+"is"==row[2]:
					analyse[2].append("GENETIF PL")
					ligne=row
			elif 10 in posib_2N:
				if mot[:-4]+'is'==row[2]:
					analyse[2].append("DATIF PL")
					analyse[2].append("ABLATIF PL")
					ligne=row
	conn.close()
	if ligne==[] or analyse==[[],[],[]]:
		return None
	else:
		return [ligne,analyse]

def comparatif(mot):
	ligne=[]
	analyse=[[],[],[]]
	declinaison=[
	["","","em","is","i","e","es","es","es","um","ibus","ibus"],
	["","","","is","i","e","a","a","a","um","ibus","ibus"]]
	conn = sqlite3.Connection("vocLatin.db")
	cur = conn.cursor()
	posib_MF=[]
	posib_N=[]
	decl=declinaison[0]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_MF.append(i)
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_MF.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_MF.append(i)
			elif mot[-1]==decl[i]:
				posib_MF.append(i)
		except:
			pass
		i+=1
	decl=declinaison[1]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_N.append(i)
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_N.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_N.append(i)
			elif mot[-1]==decl[i]:
				posib_N.append(i)
		except:
			pass
		i+=1
	for row in cur.execute("SELECT * FROM adjectif"):
		if row[4]=="" or row[4]==None:
			MF=row[2][:-1]+"ior"
			N=row[2][:-1]+"ius"
		else:
			MF=row[4]
			N=row[4][:-3]+"ius"
		if mot==MF:
			analyse[0].append("NOMINATIF SG")
			analyse[0].append("VOCAITF SG")
			analyse[1].append("NOMINATIF SG")
			analyse[1].append("VOCAITF SG")
			ligne=row
		if 2 in posib_MF:
			if mot[:-2]==MF:
				analyse[0].append("ACCUSATIF SG")
				analyse[1].append("ACCUSATIF SG")
				ligne=row
		elif 3 in posib_MF:
			if mot[:-2]==MF:
				analyse[0].append("GENITIF SG")
				analyse[1].append("GENITIF SG")
				analyse[2].append("GENETIF SG")
				ligne=row
		elif 4 in posib_MF:
			if mot[:-1]==MF:
				analyse[0].append("DATIF SG")
				analyse[1].append("DATIF SG")
				analyse[2].append("DATIF SG")
				ligne=row
		elif 5 in posib_MF:
			if mot[:-1]==MF:
				analyse[0].append("ABLATIF SG")
				analyse[1].append("ABLATIF SG")
				analyse[2].append("ABLATIF SG")
		elif 6 in posib_MF:
			if mot[:-2]==MF:
				analyse[0].append("NOMINATIF PL")
				analyse[0].append("VOCATIF PL")
				analyse[0].append("ACCUSATIF PL")
				analyse[1].append("NOMINATIF PL")
				analyse[1].append("VOCATIF PL")
				analyse[1].append("ACCUSATIF PL")
				ligne=row
		elif 9 in posib_MF:
			if mot[:-2]==MF:
				analyse[0].append("GENETIF PL")
				analyse[1].append("GENETIF PL")
				analyse[2].append("GENETIF PL")
				ligne=row
		elif 10 in posib_MF:
			if mot[:-4]==MF:
				analyse[0].append("DATIF PL")
				analyse[0].append("ABLATIF PL")
				analyse[1].append("DATIF PL")
				analyse[1].append("ABLATIF PL")
				analyse[2].append("DATIF PL")
				analyse[2].append("ABLATIF PL")
				ligne=row
		if mot==N:
			analyse[2].append("NOMINATIF SG")
			analyse[2].append("VOCATIF SG")
			analyse[2].append("ACCUSATIF SG")
			ligne=row
		elif 6 in posib_N:
			if mot[:-4]+"ius"==N:
				analyse[2].append("NOMINATIF PL")
				analyse[2].append("VOCATIF PL")
				analyse[2].append("ACCUSATIF PL")
				ligne=row
	if ligne==[] and analyse==[[],[],[]]:
		return None
	else:
		return [ligne, analyse]
def superlatif(mot):
	ligne=[]
	analyse=[[],[],[]]
	declinaison=[
	["us","e","um","i","o","o","i","i","os","orum","is","is"],
	["a","a","am","ae","ae","a","ae","ae","as","arum","is","is"],
	["um","um","um","i","o","o","a","a","a","orum","is","is"]]
	conn = sqlite3.Connection("vocLatin.db")
	cur = conn.cursor()
	posib_M=[]
	posib_F=[]
	posib_N=[]
	decl=declinaison[0]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_M.append(i)
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_M.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_M.append(i)
			elif mot[-1]==decl[i]:
				posib_M.append(i)
		except:
			pass
		i+=1
	decl=declinaison[1]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_F.append(i)
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_F.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_F.append(i)
			elif mot[-1]==decl[i]:
				posib_F.append(i)
		except:
			pass
		i+=1
	decl=declinaison[2]
	i=0
	while i<len(decl):
		try:
			if mot[-4]+mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_N.append(i)
			elif mot[-3]+mot[-2]+mot[-1]==decl[i]:
				posib_N.append(i)
			if mot[-2]+mot[-1]==decl[i]:
				posib_N.append(i)
			elif mot[-1]==decl[i]:
				posib_N.append(i)
		except:
			pass
		i+=1
	for row in cur.execute("SELECT * FROM adjectif"):
		if row[5]=="" or row[5]==None:
			if row[1][-1]=="r":
				M=row[1]+"rimus"
				F=row[1]+"rima"
				N=row[1]+"rimum"
			elif row[1][-4:]=="lis":
				M=row[1][:-2]+"limus"
				F=row[1][:-2]+"lima"
				N=row[1][:-2]+"limum"
			else:
				M=row[1][:-2]+"issimus"
				F=row[1][:-2]+"issima"
				N=row[1][:-2]+"issimum"
		else:
			M=row[5]
			F=row[5][:-2]+'a'
			N=row[5][:-2]+"um"
		if 0 in posib_F:
			if mot==F:
				analyse[1].append("NOMINATIF SG")
				analyse[1].append("VOCATIF SG")
				analyse[1].append("ABLATIF SG")
				ligne=row
		elif 9 in posib_F:
			if mot[:-4]+'a'==F:
				analyse[1].append('GENITIF PL')
				ligne=row
		elif 2 in posib_F:
			if mot[:-2]+'a'==F:
				analyse[1].append('ACCUSATIF SG')
				ligne=row
		elif 3 in posib_F:
			if mot[:-1]==F:
				analyse[1].append("GENITIF SG")
				analyse[1].append("DATIF SG")
				analyse[1].append('NOMINATIF PL')
				analyse[1].append('VOCATIF PL')
				ligne=row
		elif 8 in posib_F:
			if mot[:-2]+'a'==F:
				analyse[1].append('ACCUSATIF PL')
				ligne=row
		elif 10 in posib_F:
			if mot[:-2]+'a'==F:
				analyse[1].append('DATIF PL')
				analyse[1].append('ABLATIF PL')
				ligne=row
		if 0 in posib_M:
			if mot==M:
				analyse[0].append("NOMINATIF SG")
				ligne=row
		elif 9 in posib_M:
			if mot[:-4]+"us"==M:
				analyse[0].append("GENITIF PL")
				ligne=row
		elif 1 in posib_M:
			if mot[:-1]+"us"==M:
				analyse[0].append("VOCATIF SG")
				ligne=row
		elif 2 in posib_M:
			if mot[:-2]+"us"==M:
				analyse[0].append("ACCUSATIF SG")
				ligne=row
		elif 3 in posib_M:
			if mot[:-1]+"us"==M:
				analyse[0].append("GENITIF SG")
				analyse[0].append("NOMINATIF PL")
				analyse[0].append("VOCATIF PL")
				ligne=row
		elif 4 in posib_M:
			if mot[:-1]+"us"==M:
				analyse[0].append("DATIF SG")
				analyse[0].append("ABLATIF SG")
				ligne=row
		elif 8 in posib_M:
			if mot[:-2]+"us"==M:
				analyse[0].append("ACCUSATIF PL")
				ligne=row
		elif 10 in posib_M:
			if mot[:-2]+"us"==M:
				analyse[0].append("DATIF PL")
				analyse[0].append("ABLATIF PL")
				ligne=row
		if 9 in posib_N:
			if mot[:-4]+"um"==N:
				analyse[2].append("GENITIF PL")
				ligne=row
		elif 0 in posib_N:
			if mot==N:
				analyse[2].append("NOMINATIF SG")
				analyse[2].append("VOCATIF SG")
				analyse[2].append("ACCUSATIF SG")
				ligne=row
		elif 3 in posib_N:
			if mot[:-1]+"um"==N:
				analyse[2].append("GENITIF SG")
				ligne=row
		elif 4 in posib_N:
			if mot[:-1]+"um"==N:
				analyse[2].append("DATIF SG")
				analyse[2].append("ABLATIF SG")
				ligne=row
		elif 6 in posib_N:
			if mot[:-1]+"um"==N:
				analyse[2].append("NOMINATIF PL")
				analyse[2].append("VOCATIF PL")
				analyse[2].append("ACCUSATIF PL")
				ligne=row
		elif 10 in posib_N:
			if mot[:-2]+"um"==N:
				analyse[2].append("DATIF PL")
				analyse[2].append("ABLATIF PL")
				ligne=row
	if ligne==[] or analyse==[[],[],[]]:
		return None
	else:
		return [ligne,analyse]