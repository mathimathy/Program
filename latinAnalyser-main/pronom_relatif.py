def relatif(mot):
	trad=""
	analyse=[[],[],[]]
	if mot=="qui":
		trad="qui"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("NOMINATIF PL")
	elif mot=="quem":
		trad="que"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="cuius":
		trad="dont"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="cui":
		trad="à,pourquoi"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
	elif mot=="quo":
		trad="prép + qui"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif mot=="quod":
		trad="qui,que"
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="quae":
		trad="qui,que"
		analyse[1].append("NOMINATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("NOMINATIF PL")
	elif mot=="qua":
		trad="prép + qui"
		analyse[1].append("ABLATIF SG")
	elif mot=="quos":
		trad="que"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="quorum":
		trad="dont"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="quibus":
		trad="à,pourquoi,prép + qui"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="quas":
		trad="que"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="quarum":
		trad="dont"
		analyse[1].append("GENITIF PL")
	elif mot=="quam":
		trad="que"
		analyse[1].append("ACCUSATIF SG")
	if trad=="" and analyse==[[],[],[]]:
		return None
	else:
		return [trad,analyse]