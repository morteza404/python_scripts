import pymysql as pm 

db = pm.connect('localhost', 'root', '1234', 'morteza')

cur = db.cursor()

q = cur.execute('select * from emp')

for row in q:
    print(row)

db.close()    