from flask import Flask,render_template
import mysql.connector
# from mysql.connector import errorcode


cnx = mysql.connector.connect(user='root', database='test')
print('Connected Successfully.')
cursor = cnx.cursor()
query = ("SELECT * FROM dataset")
cursor.execute(query)
# for row in cursor.fetchall():
#     print(row)
data = cursor.fetchall()


# cursor.close()
# cnx.close()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', data=data)

if __name__ == "__main__":
    app.run()    