import sqlite3
db=sqlite3.connect("log.sqlite")
for row in db.execute("select * from users"):
    print(row)
db.close()