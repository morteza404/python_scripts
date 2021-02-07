import sqlite3
import time

def db_connection():
    return sqlite3.connect("17ed53db6edf25d8f81a37418d5a6d71.db")

def count():    
    with db_connection() as db:        
        query = "SELECT COUNT(*) FROM object;"
        cur = db.cursor()
        cur.execute(query)
        return cur.fetchone()[0]        

if __name__ == "__main__":
    start = time.time()
    count = count()
    end = time.time()
    duration = end -start
    with open("get_object.txt", "a") as target:
        target.write(str(count) + "," + str(duration) + "\n")

