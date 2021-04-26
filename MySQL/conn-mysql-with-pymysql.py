import pymysql


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')

cur = conn.cursor()

cur.execute("SELECT * FROM people")

# print(cur.description)
# print()

for row in cur:
    print(row)

cur.close()
conn.close()