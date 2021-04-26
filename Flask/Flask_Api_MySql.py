from flask import Flask

import mysql.connector


app = Flask(__name__)

@app.route('/api/<username>/<password>')
def home(username, password):
    cnx = mysql.connector.connect(user='root', database='test')

    print('Connected Successfully.')

    cursor = cnx.cursor()

    query = ("SELECT * FROM dataset where username = %s AND password = %s", (username,password))

    cursor.execute(query)

    for row in cursor.fetchall():
        return row
    

if __name__ == "__main__":
    app.run()    