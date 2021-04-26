# CONNECT TO DB

# import mysql.connector
# cnx = mysql.connector.connect(user='root',password='',host='localhost',database='test')

# import mysql.connector
# from mysql.connector import errorcode

# try:
#   cnx = mysql.connector.connect(user='root',database='test')
#   print('Connected Successfully.')
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cnx.close()


# SELECT DATA

# import mysql.connector

# cnx = mysql.connector.connect(user='root', database='test')
# cursor = cnx.cursor()

# query = ("SELECT * FROM member_details ")

# cursor.execute(query)

# for row in cursor.fetchall():
#   print(row)

# cursor.close()
# cnx.close() 


# SELECT DATA

import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', database='test')
    print('Connected Successfully.')
    cursor = cnx.cursor()
    query = ("SELECT * FROM member_details ")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    cnx.close()