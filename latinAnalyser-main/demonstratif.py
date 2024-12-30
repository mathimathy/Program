def demonstratif(mot):
	analyse=[[],[],[]]
	trad=""
	if mot=="hic":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="hunc":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="huius":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="huic":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
	elif mot=="hoc":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="haec":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
	elif mot=="hac":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("ABLATIF SG")
	elif mot=="hi":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="hos":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="horum":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="his":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="hae":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="has":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="harum":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("GENITIF PL")
	elif mot=="hanc":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("ACCUSATIF SG")


	if mot=="iste":
		trad="celui-là, celle-là, ceux-là"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="istum":
		trad="celui-là, celle-là, ceux-là"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="istius":
		trad="celui-là, celle-là, ceux-là"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="isti":
		trad="celui-là, celle-là, ceux-là"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="isto":
		trad="celui-là, celle-là, ceux-là"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif mot=="istud":
		trad="celui-là, celle-là, ceux-là"
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="ista":
		trad="celui-là, celle-là, ceux-là"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="istos":
		trad="celui-là, celle-là, ceux-là"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="ostorum":
		trad="celui-là, celle-là, ceux-là"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="istis":
		trad="celui-là, celle-là, ceux-là"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="istae":
		trad="celui-là, celle-là, ceux-là"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="istas":
		trad="celui-là, celle-là, ceux-là"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="istarum":
		trad="celui-là, celle-là, ceux-là"
		analyse[1].append("GENITIF PL")
	elif mot=="istam":
		trad="celui-là, celle-là, ceux-là"
		analyse[1].append("ACCUSATIF SG")


	if mot=="ille":
		trad="celui-là,celle-là,ceux-là"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="illum":
		trad="celui-là,celle-là,ceux-là"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="illius":
		trad="celui-là,celle-là,ceux-là"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="illi":
		trad="celui-là,celle-là,ceux-là"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="illo":
		trad="celui-là,celle-là,ceux-là"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif mot=="illud":
		trad="celui-là, celle-là, ceux-là"
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="illa":
		trad="celui-là,celle-là,ceux-là"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="illos":
		trad="celui-là,celle-là,ceux-là"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="illorum":
		trad="celui-là,celle-là,ceux-là"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="illis":
		trad="celui-là,celle-là,ceux-là"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="illae":
		trad="celui-là,celle-là,ceux-là"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="illas":
		trad="celui-là,celle-là,ceux-là"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="illarum":
		trad="celui-là,celle-là,ceux-là"
		analyse[1].append("GENITIF PL")
	elif mot=="illam":
		trad="celui-là, celle-là, ceux-là"
		analyse[1].append("ACCUSATIF SG")
	

	if mot=="is":
		trad="ce,cette,cet"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="eum":
		trad="ce,cette,cet"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="eius":
		trad="ce,cette,cet"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="ei":
		trad="ce,cette,cet"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="eo":
		trad="ce,cette,cet"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif trad=="id":
		trad="ce,cette,cet"
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="ea":
		trad="ce,cette,cet"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="ii":
		trad="ce,cette,cet"
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="eos":
		trad="ce,cette,cet"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="eorum":
		trad="ce,cette,cet"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="iis" or mot=="eis":
		trad="ce,cette,cet"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="eae":
		trad="ce,cette,cet"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="eas":
		trad="ce,cette,cet"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="earum":
		trad="ce,cette,cet"
		analyse[1].append("GENITIF PL")
	elif mot=="eam":
		trad="ce,cette,cet"
		analyse[1].append("ACCUSATIF SG")
	

	if mot=="ipse":
		trad="lui-même,elle-même"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="ipsum":
		trad="lui-même,elle-même"
		analyse[0].append("ACCUSATIF SG")
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="ipsius":
		trad="lui-même,elle-même"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="ipsi":
		trad="lui-même,elle-même"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="ipso":
		trad="lui-même,elle-même"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif mot=="ipsa":
		trad="lui-même,elle-même"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="ipsos":
		trad="lui-même,elle-même"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="ipsorum":
		trad="lui-même,elle-même"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="ipsis":
		trad="lui-même,elle-même"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="ipsae":
		trad="lui-même,elle-même"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="ipsas":
		trad="lui-même,elle-même"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="ipsarum":
		trad="lui-même,elle-même"
		analyse[1].append("GENITIF PL")
	elif mot=="ipsam":
		trad="lui-même,elle-même"
		analyse[1].append("ACCUSATIF SG")
	


	if mot=="idem":
		trad="le même,la même"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="eiudem":
		trad="le même,la même"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="eiusdem":
		trad="le même,la même"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="eidem":
		trad="le même,la même"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="eodem":
		trad="le même,la même"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif mot=="eadem":
		trad="le même,la même"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="iidem":
		trad="le même,la même"
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="eosdem":
		trad="le même,la même"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="eorundem":
		trad="le même,la même"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="iisdem" or mot=="eisdem":
		trad="le même,la même"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="eaedem":
		trad="le même,la même"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="easdem":
		trad="le même,la même"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="earundem":
		trad="le même,la même"
		analyse[1].append("GENITIF PL")
	elif mot=="eandem":
		trad="le même,la même"
		analyse[1].append("ACCUSATIF SG")
	if trad=="" and analyse==[[],[],[]]:
		return None
	else:
		return [trad,analyse]