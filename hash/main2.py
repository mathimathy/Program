from random import randint
def ph_vers_aa(ph):
	a=['me']
	for i in range(0,len(ph)):
		if ph[i]=='0':
			a.append('ly')
			a.append('as')
		if ph[i]=='1':
			a.append('ly')
			a.append('th')
		if ph[i]=='2':
			a.append('ly')
			a.append('is')
		if ph[i]=='3':
			a.append('ly')
			a.append('ar')
		if ph[i]=='4':
			a.append('ly')
			a.append('se')
		if ph[i]=='5':
			a.append('ly')
			a.append('gl')
		if ph[i]=='6':
			a.append('ly')
			a.append('hi')
		if ph[i]=='7':
			a.append('ly')
			a.append('pr')
		if ph[i]=='8':
			a.append('ly')
			a.append('le')
		if ph[i]=='9':
			a.append('ly')
			a.append('ty')
		if ph[i]=='a':
			a.append('ly')
			a.append('ph')
		if ph[i]=='b':
			a.append('ly')
			a.append('cy')
		if ph[i]=='c':
			a.append('ly')
			a.append('tr')
		if ph[i]=='d':
			a.append('ly')
			a.append('ag')
		if ph[i]=='e':
			a.append('ly')
			a.append('aa')
		if ph[i]=='f':
			a.append('ly')
			a.append('al')
		if ph[i]=='g':
			a.append('ly')
			a.append('va')
		if ph[i]=='h':
			a.append('as')
			a.append('ly')
		if ph[i]=='i':
			a.append('as')
			a.append('th')
		if ph[i]=='j':
			a.append('as')
			a.append('is')
		if ph[i]=='k':
			a.append('as')
			a.append('ar')
		if ph[i]=='l':
			a.append('as')
			a.append('se')
		if ph[i]=='m':
			a.append('as')
			a.append('gl')
		if ph[i]=='n':
			a.append('as')
			a.append('hi')
		if ph[i]=='o':
			a.append('as')
			a.append('pr')
		if ph[i]=='p':
			a.append('as')
			a.append('le')
		if ph[i]=='q':
			a.append('as')
			a.append('ty')
		if ph[i]=='r':
			a.append('as')
			a.append('ph')
		if ph[i]=='s':
			a.append('as')
			a.append('cy')
		if ph[i]=='t':
			a.append('as')
			a.append('tr')
		if ph[i]=='u':
			a.append('as')
			a.append('ag')
		if ph[i]=='v':
			a.append('as')
			a.append('aa')
		if ph[i]=='w':
			a.append('as')
			a.append('al')
		if ph[i]=='x':
			a.append('as')
			a.append('va')
		if ph[i]=='y':
			a.append('th')
			a.append('ly')
		if ph[i]=='z':
			a.append('th')
			a.append('as')
		if ph[i]=='A':
			a.append('th')
			a.append('is')
		if ph[i]=='B':
			a.append('th')
			a.append('ar')
		if ph[i]=='C':
			a.append('th')
			a.append('se')
		if ph[i]=='D':
			a.append('th')
			a.append('gl')
		if ph[i]=='E':
			a.append('th')
			a.append('hi')
		if ph[i]=='F':
			a.append('th')
			a.append('pr')
		if ph[i]=='G':
			a.append('th')
			a.append('le')
		if ph[i]=='H':
			a.append('th')
			a.append('ty')
		if ph[i]=='I':
			a.append('th')
			a.append('ph')
		if ph[i]=='J':
			a.append('th')
			a.append('cy')
		if ph[i]=='K':
			a.append('th')
			a.append('tr')
		if ph[i]=='L':
			a.append('th')
			a.append('ag')
		if ph[i]=='M':
			a.append('th')
			a.append('aa')
		if ph[i]=='N':
			a.append('th')
			a.append('al')
		if ph[i]=='O':
			a.append('th')
			a.append('va')
		if ph[i]=='P':
			a.append('is')
			a.append('ly')
		if ph[i]=='Q':
			a.append('is')
			a.append('as')
		if ph[i]=='R':
			a.append('is')
			a.append('th')
		if ph[i]=='S':
			a.append('is')
			a.append('se')
		if ph[i]=='T':
			a.append('is')
			a.append('ar')
		if ph[i]=='U':
			a.append('is')
			a.append('gl')
		if ph[i]=='V':
			a.append('is')
			a.append('hi')
		if ph[i]=='W':
			a.append('is')
			a.append('pr')
		if ph[i]=='X':
			a.append('is')
			a.append('le')
		if ph[i]=='Y':
			a.append('is')
			a.append('ty')
		if ph[i]=='Z':
			a.append('is')
			a.append('ph')
		if ph[i]=='à':
			a.append('is')
			a.append('cy')
		if ph[i]=='é':
			a.append('is')
			a.append('tr')
		if ph[i]=='è':
			a.append('is')
			a.append('ag')
		if ph[i]=='ç':
			a.append('is')
			a.append('aa')
		if ph[i]=='À':
			a.append('is')
			a.append('al')
		if ph[i]=='É':
			a.append('is')
			a.append('va')
		if ph[i]=='È':
			a.append('ar')
			a.append('ly')
		if ph[i]=='@':
			a.append('ar')
			a.append('as')
		if ph[i]=='#':
			a.append('ar')
			a.append('th')
		if ph[i]=='$':
			a.append('ar')
			a.append('is')
		if ph[i]=='ù':
			a.append('ar')
			a.append('se')
		if ph[i]=='Ù':
			a.append('ar')
			a.append('gl')
		if ph[i]=='£':
			a.append('ar')
			a.append('hi')
		if ph[i]=='€':
			a.append('ar')
			a.append('pr')
		if ph[i]=='&':
			a.append('ar')
			a.append('le')
		if ph[i]=='"':
			a.append('ar')
			a.append('ty')
		if ph[i]=='\'':
			a.append('ar')
			a.append('ph')
		if ph[i]=='(':
			a.append('ar')
			a.append('cy')
		if ph[i]==')':
			a.append('ar')
			a.append('tr')
		if ph[i]=='{':
			a.append('ar')
			a.append('ag')
		if ph[i]=='}':
			a.append('ar')
			a.append('aa')
		if ph[i]=='[':
			a.append('ar')
			a.append('al')
		if ph[i]==']':
			a.append('ar')
			a.append('va')
		if ph[i]=='%':
			a.append('se')
			a.append('ly')
		if ph[i]=='=':
			a.append('se')
			a.append('as')
		if ph[i]=='+':
			a.append('se')
			a.append('th')
		if ph[i]=='-':
			a.append('se')
			a.append('is')
		if ph[i]=='/':
			a.append('se')
			a.append('ar')
		if ph[i]=='*':
			a.append('se')
			a.append('gl')
		if ph[i]=='_':
			a.append('se')
			a.append('hi')
		if ph[i]=='!':
			a.append('se')
			a.append('pr')
		if ph[i]=='?':
			a.append('se')
			a.append('le')
		if ph[i]=='.':
			a.append('se')
			a.append('ty')
		if ph[i]==':':
			a.append('se')
			a.append('ph')
		if ph[i]==';':
			a.append('se')
			a.append('cy')
		if ph[i]==',':
			a.append('se')
			a.append('tr')
		if ph[i]=='<':
			a.append('se')
			a.append('ag')
		if ph[i]=='>':
			a.append('se')
			a.append('aa')
		if ph[i]=='\\':
			a.append('se')
			a.append('al')
		if ph[i]==' ':
			a.append('se')
			a.append('va')
		print(a)
	a.append('s')
	return a
def aa_vers_ph(aa):
	ph=''
	for i in range(1,len(aa)-1,2):
		if aa[i]+aa[i+1] == 'lyas':
			ph+='0'
		if aa[i]+aa[i+1] == 'lyth':
			ph+='1'
		if aa[i]+aa[i+1] == 'lyis':
			ph+='2'
		if aa[i]+aa[i+1] == 'lyar':
			ph+='3'
		if aa[i]+aa[i+1] == 'lyse':
			ph+='4'
		if aa[i]+aa[i+1] == 'lygl':
			ph+='5'
		if aa[i]+aa[i+1] == 'lyhi':
			ph+='6'
		if aa[i]+aa[i+1] == 'lypr':
			ph+='7'
		if aa[i]+aa[i+1] == 'lyle':
			ph+='8'
		if aa[i]+aa[i+1] == 'lyty':
			ph+='9'
		if aa[i]+aa[i+1] == 'lyph':
			ph+='a'
		if aa[i]+aa[i+1] == 'lycy':
			ph+='b'
		if aa[i]+aa[i+1] == 'lytr':
			ph+='c'
		if aa[i]+aa[i+1] == 'lyag':
			ph+='d'
		if aa[i]+aa[i+1] == 'lyaa':
			ph+='e'
		if aa[i]+aa[i+1] == 'lyal':
			ph+='f'
		if aa[i]+aa[i+1] == 'lyva':
			ph+='g'
		if aa[i]+aa[i+1] == 'asly':
			ph+='h'
		if aa[i]+aa[i+1] == 'asth':
			ph+='i'
		if aa[i]+aa[i+1] == 'asis':
			ph+='j'
		if aa[i]+aa[i+1] == 'asar':
			ph+='k'
		if aa[i]+aa[i+1] == 'asse':
			ph+='l'
		if aa[i]+aa[i+1] == 'asgl':
			ph+='m'
		if aa[i]+aa[i+1] == 'ashi':
			ph+='n'
		if aa[i]+aa[i+1] == 'aspr':
			ph+='o'
		if aa[i]+aa[i+1] == 'asle':
			ph+='p'
		if aa[i]+aa[i+1] == 'asty':
			ph+='q'
		if aa[i]+aa[i+1] == 'asph':
			ph+='r'
		if aa[i]+aa[i+1] == 'ascy':
			ph+='s'
		if aa[i]+aa[i+1] == 'astr':
			ph+='t'
		if aa[i]+aa[i+1] == 'asag':
			ph+='u'
		if aa[i]+aa[i+1] == 'asaa':
			ph+='v'
		if aa[i]+aa[i+1] == 'asal':
			ph+='w'
		if aa[i]+aa[i+1] == 'asva':
			ph+='x'
		if aa[i]+aa[i+1] == 'thly':
			ph+='y'
		if aa[i]+aa[i+1] == 'thas':
			ph+='z'
		if aa[i]+aa[i+1] == 'this':
			ph+='A'
		if aa[i]+aa[i+1] == 'thar':
			ph+='B'
		if aa[i]+aa[i+1] == 'thse':
			ph+='C'
		if aa[i]+aa[i+1] == 'thgl':
			ph+='D'
		if aa[i]+aa[i+1] == 'thhi':
			ph+='E'
		if aa[i]+aa[i+1] == 'thpr':
			ph+='F'
		if aa[i]+aa[i+1] == 'thle':
			ph+='G'
		if aa[i]+aa[i+1] == 'thty':
			ph+='H'
		if aa[i]+aa[i+1] == 'thph':
			ph+='I'
		if aa[i]+aa[i+1] == 'thcy':
			ph+='J'
		if aa[i]+aa[i+1] == 'thtr':
			ph+='K'
		if aa[i]+aa[i+1] == 'thag':
			ph+='L'
		if aa[i]+aa[i+1] == 'thaa':
			ph+='M'
		if aa[i]+aa[i+1] == 'thal':
			ph+='N'
		if aa[i]+aa[i+1] == 'thva':
			ph+='O'
		if aa[i]+aa[i+1] == 'isly':
			ph+='P'
		if aa[i]+aa[i+1] == 'isas':
			ph+='Q'
		if aa[i]+aa[i+1] == 'isth':
			ph+='R'
		if aa[i]+aa[i+1] == 'isse':
			ph+='S'
		if aa[i]+aa[i+1] == 'isar':
			ph+='T'
		if aa[i]+aa[i+1] == 'isgl':
			ph+='U'
		if aa[i]+aa[i+1] == 'ishi':
			ph+='V'
		if aa[i]+aa[i+1] == 'ispr':
			ph+='W'
		if aa[i]+aa[i+1] == 'isle':
			ph+='X'
		if aa[i]+aa[i+1] == 'isty':
			ph+='Y'
		if aa[i]+aa[i+1] == 'isph':
			ph+='Z'
		if aa[i]+aa[i+1] == 'iscy':
			ph+='à'
		if aa[i]+aa[i+1] == 'istr':
			ph+='é'
		if aa[i]+aa[i+1] == 'isag':
			ph+='è'
		if aa[i]+aa[i+1] == 'isaa':
			ph+='ç'
		if aa[i]+aa[i+1] == 'isal':
			ph+='À'
		if aa[i]+aa[i+1] == 'isva':
			ph+='É'
		if aa[i]+aa[i+1] == 'arly':
			ph+='È'
		if aa[i]+aa[i+1] == 'aras':
			ph+='@'
		if aa[i]+aa[i+1] == 'arth':
			ph+='#'
		if aa[i]+aa[i+1] == 'aris':
			ph+='$'
		if aa[i]+aa[i+1] == 'arse':
			ph+='ù'
		if aa[i]+aa[i+1] == 'argl':
			ph+='Ù'
		if aa[i]+aa[i+1] == 'arhi':
			ph+='£'
		if aa[i]+aa[i+1] == 'arpr':
			ph+='€'
		if aa[i]+aa[i+1] == 'arle':
			ph+='&'
		if aa[i]+aa[i+1] == 'arty':
			ph+='"'
		if aa[i]+aa[i+1] == 'arph':
			ph+='\''
		if aa[i]+aa[i+1] == 'arcy':
			ph+='('
		if aa[i]+aa[i+1] == 'artr':
			ph+=')'
		if aa[i]+aa[i+1] == 'arag':
			ph+='{'
		if aa[i]+aa[i+1] == 'araa':
			ph+='}'
		if aa[i]+aa[i+1] == 'aral':
			ph+='['
		if aa[i]+aa[i+1] == 'arva':
			ph+=']'
		if aa[i]+aa[i+1] == 'sely':
			ph+='%'
		if aa[i]+aa[i+1] == 'seas':
			ph+='='
		if aa[i]+aa[i+1] == 'seth':
			ph+='+'
		if aa[i]+aa[i+1] == 'seis':
			ph+='-'
		if aa[i]+aa[i+1] == 'sear':
			ph+='/'
		if aa[i]+aa[i+1] == 'segl':
			ph+='*'
		if aa[i]+aa[i+1] == 'sehi':
			ph+='_'
		if aa[i]+aa[i+1] == 'sepr':
			ph+='!'
		if aa[i]+aa[i+1] == 'sele':
			ph+='?'
		if aa[i]+aa[i+1] == 'sety':
			ph+='.'
		if aa[i]+aa[i+1] == 'seph':
			ph+=':'
		if aa[i]+aa[i+1] == 'secy':
			ph+=';'
		if aa[i]+aa[i+1] == 'setr':
			ph+=','
		if aa[i]+aa[i+1] == 'seag':
			ph+='<'
		if aa[i]+aa[i+1] == 'seaa':
			ph+='>'
		if aa[i]+aa[i+1] == 'seal':
			ph+='\\'
		if aa[i]+aa[i+1] == 'seva':
			ph+=' '
		print(ph)
	return ph
def arm_vers_aa(arm):
	aa=[]
	for i in range(0,len(arm),3):
		if arm[i:i+3]=='aaa' or arm[i:i+3]=='aag':
			aa.append('ly')
		elif arm[i:i+3]=='aac' or arm[i:i+3]=='aau':
			aa.append('as')
		elif arm[i:i+3]=='aca' or arm[i:i+3]=='acc' or arm[i:i+3]=='acu' or arm[i:i+3]=='acg':
			aa.append('th')
		elif arm[i:i+3]=='aua' or arm[i:i+3]=='auc' or arm[i:i+3]=='auu':
			aa.append('is')
		elif arm[i:i+3]=='aug':
			aa.append('me')
		elif arm[i:i+3]=='aga' or arm[i:i+3]=='agg' or arm[i:i+3]=='cga' or arm[i:i+3]=='cgc' or arm[i:i+3]=='cgu' or arm[i:i+3]=='cgg':
			aa.append('ar')
		elif arm[i:i+3]=='agc' or arm[i:i+3]=='agu' or arm[i:i+3]=='uac' or arm[i:i+3]=='ucc' or arm[i:i+3]=='ucu' or arm[i:i+3]=='ucg':
			aa.append('se')
		elif arm[i:i+3]=='caa' or arm[i:i+3]=='cag' or arm[i:i+3]=='gga' or arm[i:i+3]=='ggc' or arm[i:i+3]=='ggu' or arm[i:i+3]=='ggg':
			aa.append('gl')
		elif arm[i:i+3]=='cac' or arm[i:i+3]=='cau':
			aa.append('hi')
		elif arm[i:i+3]=='cca' or arm[i:i+3]=='ccc' or arm[i:i+3]=='ccu' or arm[i:i+3]=='ccg':
			aa.append('pr')
		elif arm[i:i+3]=='cua' or arm[i:i+3]=='cuc' or arm[i:i+3]=='cuu' or arm[i:i+3]=='cug' or arm[i:i+3]=='uua' or arm[i:i+3]=='uug':
			aa.append('le')
		elif arm[i:i+3]=='uac' or arm[i:i+3]=='uau':
			aa.append('ty')
		elif arm[i:i+3]=='uuc' or arm[i:i+3]=='uuu':
			aa.append('ph')
		elif arm[i:i+3]=='ugc' or arm[i:i+3]=='ugu':
			aa.append('cy')
		elif arm[i:i+3]=='ugg':
			aa.append('tr')
		elif arm[i:i+3]=='gaa' or arm[i:i+3]=='gag':
			aa.append('ag')
		elif arm[i:i+3]=='gac' or arm[i:i+3]=='gau':
			aa.append('aa')
		elif arm[i:i+3]=='gca' or arm[i:i+3]=='gcc' or arm[i:i+3]=='gcu' or arm[i:i+3]=='gcg':
			aa.append('al')
		elif arm[i:i+3]=='gua' or arm[i:i+3]=='guc' or arm[i:i+3]=='guu' or arm[i:i+3]=='gug':
			aa.append('va')
		elif arm[i:i+3]=='uaa' or arm[i:i+3]=='uag' or arm[i:i+3]=='uga':
			aa.append('s')
		print(aa)
	return aa
def aa_vers_arm(aa):
	arm=''
	for i in range(0,len(aa)-1):
		if aa[i]=='ly':
			if randint(0,1):
				arm+='aaa'
			else:
				arm+='aag'
		elif aa[i]=='as':
			if randint(0,1):
				arm+='aac'
			else:
				arm+='aau'
		elif aa[i]=='ar':
			x=randint(0,5)
			if x==0:
				arm+='aga'
			elif x==1:
				arm+='agg'
			elif x==1:
				arm+='cga'
			elif x==1:
				arm+='cgc'
			elif x==1:
				arm+='cgu'
			else:
				arm+='cgg'
		elif aa[i]=='th':
			x=randint(0,3)
			if x==0:
				arm+='aca'
			elif x==1:
				arm+='acc'
			elif x==2:
				arm+='acu'
			else:
				arm+='acg'
		elif aa[i]=='is':
			x=randint(0,2)
			if x==0:
				arm+='aua'
			elif x==1:
				arm+='auc'
			else:
				arm+='auu'
		elif aa[i]=='me':
			arm+='aug'
		elif aa[i]=='th':
			x=randint(0,5)
			if x==0:
				arm+='aga'
			elif x==1:
				arm+='agg'
			elif x==2:
				arm+='cga'
			elif x==3:
				arm+='cgc'
			elif x==4:
				arm+='cgu'
			else:
				arm+='cgg'
		elif aa[i]=='se':
			x=randint(0,5)
			if x==0:
				arm+='agc'
			elif x==1:
				arm+='agu'
			elif x==2:
				arm+='uca'
			elif x==3:
				arm+='ucc'
			elif x==4:
				arm+='ucu'
			else:
				arm+='ucg'
		elif aa[i]=='gl':
			x=randint(0,5)
			if x==0:
				arm+='caa'
			elif x==1:
				arm+='cag'
			elif x==2:
				arm+='gga'
			elif x==3:
				arm+='ggc'
			elif x==4:
				arm+='ggu'
			else:
				arm+='ggg'
		elif aa[i]=='hi':
			if randint(0,1):
				arm+='cac'
			else:
				arm+='cau'
		elif aa[i]=='pr':
			x=randint(0,3)
			if x==0:
				arm+='cca'
			elif x==1:
				arm+='ccc'
			elif x==2:
				arm+='ccu'
			else:
				arm+='ccg'
		elif aa[i]=='le':
			x=randint(0,5)
			if x==0:
				arm+='cua'
			elif x==1:
				arm+='cuc'
			elif x==2:
				arm+='cuu'
			elif x==3:
				arm+='cug'
			elif x==4:
				arm+='uua'
			else:
				arm+='uug'
		elif aa[i]=='ty':
			if randint(0,1):
				arm+='uac'
			else:
				arm+='uau'
		elif aa[i]=='ph':
			if randint(0,1):
				arm+='uuc'
			else:
				arm+='uuu'
		elif aa[i]=='cy':
			if randint(0,1):
				arm+='ugc'
			else:
				arm+='ugu'
		elif aa[i]=='tr':
			arm+='ugg'
		elif aa[i]=='ag':
			if randint(0,1):
				arm+='gaa'
			else:
				arm+='gag'
		elif aa[i]=='aa':
			if randint(0,1):
				arm+='gac'
			else:
				arm+='gau'
		elif aa[i]=='al':
			x=randint(0,3)
			if x==0:
				arm+='gca'
			elif x==1:
				arm+='gcc'
			elif x==2:
				arm+='gcu'
			else:
				arm+='gcg'
		elif aa[i]=='va':
			x=randint(0,3)
			if x==0:
				arm+='gua'
			elif x==1:
				arm+='guc'
			elif x==2:
				arm+='guu'
			else:
				arm+='gug'
		print(arm)
	x=randint(0,2)
	if x==0:
		arm+='uaa'
	elif x==1:
		arm+='uag'
	else:
		arm+='uga'
	return arm
def adn_vers_arm(adn):
	arm=''
	for i in range(0,len(adn)):
		if adn[i]=='a':
			arm+='u'
		elif adn[i]=='t':
			arm+='a'
		elif adn[i]=='g':
			arm+='c'
		elif adn[i]=='c':
			arm+='g'
		print(arm)
	return arm
def arm_vers_adn(arm):
	adn=''
	for i in range(0,len(arm)):
		if arm[i]=='a':
			adn+='t'
		elif arm[i]=='u':
			adn+='a'
		elif arm[i]=='g':
			adn+='c'
		elif arm[i]=='c':
			adn+='g'
		print(adn)
	return adn