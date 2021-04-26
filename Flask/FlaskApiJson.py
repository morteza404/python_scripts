# from flask import Flask, jsonify
# import psycopg2


# app = Flask(__name__)

# @app.route('/{lat}/{lon}')
# def index():
#     pass

# jsonresult = {}
# a = ""
# b = ""
# inputnet = '11'
# inputlac = '2224'
# inputcell = '11365'
# hostname = 'localhost'
# username = 'postgres'
# password = '123'
# database = 'final2'
# # set connection
# conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM laccell2 WHERE 'Net'=%s and 'Area'=%s and 'Cell'=%s ",(inputnet,inputlac,inputcell))
# # cursor.execute(f"SELECT * FROM laccell2 WHERE 'Net'={inputnet} and 'Area'={inputlac} and 'Cell'={inputcell}")
# for Id, Radio, Mcc, Net, Area, Cell, Unit, Lon, Lat, Range, Samples, Changeable, Created, Updated, AverageSignal, Lonlat in cursor.fetchall() :
# 	if Lat!="" and Lon!="":
# 		jsonresult['lat'] = Lat
# 		a = Lat
# 		jsonresult['lon'] = Lon
# 		b = Lon
# 		break
	
	
# 	if a=="" or b=="":
# 		cursor.execute('INSERT INTO notexist (net,lac,cell) VALUES (%s,%s,%s);',(inputnet,inputlac,inputcell))
# 	cursor.close()
# 	conn.commit()
# 	conn.close()
# 	print(jsonresult)


#     if __name__ == '__main__':
#         app.run()

from flask import Flask

import psycopg2


app = Flask(__name__)

@app.route('/api/<net>/<lac>/<cell>')
def home(net, lac, cell):
    cnx = psycopg2.connect(host='localhost', user='postgres', password='123', database='final2')

    # print('Connected Successfully.')

    cursor = cnx.cursor()

    cursor.execute("SELECT * FROM laccell2 WHERE 'Net' = %s AND 'Area' = %s AND 'Cell' = %s", (net, lac, cell))

    for row in cursor.fetchall():
        return row
    

if __name__ == "__main__":
    app.run()    