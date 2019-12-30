import sqlite3

def PersonDatabase():
	con = sqlite3.connect("database.db")
	con.execute("CREATE TABLE IF NOT EXISTS persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, address text, mobile_no text, date text, time text, amount text)")
	con.commit()
	con.close()

def addData(name, address, mobile_no, date, time, amount):
	con = sqlite3.connect("database.db")
	status = con.execute("INSERT INTO persons(name, address, mobile_no, date, time, amount) VALUES(?,?,?,?,?,?)", (name, address, mobile_no, date, time, amount))
	con.commit()
	con.close()
	if status:
		return True
	else:
		return False

def deleteData(id):
	con = sqlite3.connect("database.db")
	con.execute("DELETE FROM persons WHERE id=?", (id,))
	con.commit()
	con.close()

def searchData(name="", address="", mobile_no="", date="", time="", amount=""):
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM persons WHERE name=? OR address=? OR mobile_no=? OR date=? OR time=? OR amount=?", (name, address, mobile_no, date, time, amount))
	rows = cur.fetchall()
	con.close()
	return rows

def displayData():
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM persons")
	rows = cur.fetchall()
	con.close()
	return rows


PersonDatabase()