import MySQLdb

db = MySQLdb.connect("localhost", "root", "otokon", "vfly")
cur = db.cursor()

cur.execute("select*from gps order by id desc limit 1")

row = cur.fetchone()
print row[2]
