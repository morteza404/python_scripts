import os
import psycopg2
from flask import Flask
# from urllib.parse import urlparse
from os.path import exists
from os import makedirs

# url = urlparse(os.environ.get('DATABASE_URL'))

# schema = "schema.sql"
conn = psycopg2.connect(dbname='final2', user='postgres', password='123' ,host='localhost')

cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/latlon')
def contacts():
    try:
        cur.execute("SELECT * FROM laccell2 LIMIT 10")
        rows = cur.fetchall()
        # response = ''
        my_list = []
        for row in rows:
            my_list.append(row)

        return my_list
    except Exception as e:
        print(e)
        return []

if __name__ == '__main__':
    app.run()