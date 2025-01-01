import sqlite3

def conj(mot):
	conn = sqlite3.Connection("vocLatin.db")
	cur = conn.cursor()
	ligne=[]
	for row in cur.execute('SELECT * FROM conjonction'):
		if row[1]==mot:
			ligne=row
	conn.close()
	if ligne==[]:
		return None
	else:
		return ligne