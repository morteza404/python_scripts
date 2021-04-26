import sqlite3
db = sqlite3.connect("log.sqlite")
db.execute("create table if not exists log(user text, pass text)")
db.execute("insert into log(user,pass) values('mori','123')")
db.execute("insert into log(user,pass) values('ada','456')")
db.execute("insert into log(user,pass) values('sss','789')")
db.execute("insert into log(user,pass) values('mmm','101')")

cursor = db.cursor()
cursor.execute("select * from log")

print(cursor.fetchall())

for row in cursor:
    print(row)
    print('*'*20)
db.commit()
db.close()

