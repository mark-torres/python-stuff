import mydb

db = mydb.MyDB('test.db')

db.query("DROP TABLE IF EXISTS temps")
db.query("CREATE TABLE temps(date text, temp int)")

db.query("INSERT INTO temps VALUES('20/3/2015', 29)")
db.query("INSERT INTO temps VALUES('20/4/2015', 39)")
db.query("INSERT INTO temps VALUES('20/5/2015', 22)")
db.query("INSERT INTO temps VALUES('20/6/2015', 32)")
db.query("INSERT INTO temps VALUES('20/7/2015', 40)")
db.query("INSERT INTO temps VALUES('20/8/2015', 21)")

db.query("select * from temps")
rows = db.fetchall()
for row in rows:
	print("%s %s" % (row['date'], row['temp']))

db.query("SELECT AVG(temp) AS avg_temp FROM temps")
row = db.fetchone()
print("The average temperature was %s" % row['avg_temp'])
