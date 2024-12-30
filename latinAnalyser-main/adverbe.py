import sqlite3

def adverbe(mot):
	conn = sqlite3.Connection("vocLatin.db")
	cur = conn.cursor()
	ligne=[]
	for row in cur.execute('SELECT * FROM adverbe'):
		if row[1]==mot:
			ligne=row
	conn.close()
	if ligne==[]:
		return None
	else:
		return ligne