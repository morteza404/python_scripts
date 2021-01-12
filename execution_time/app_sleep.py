import sqlite3
import time
import subprocess

def db_connection():
    return sqlite3.connect("test2.db")

def create():     
    with db_connection() as db:        
        try:        
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Student (
                                                  Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                  Name VARCHAR(20),
                                                  Address VARCHAR(20)
                                                  )
                        """)
            print ("table created successfully")
        except:
            print ("error in operation")
            db.rollback()

def insert(name, address):     
    with db_connection() as db:        
        query="INSERT INTO Student (Name, Address) VALUES(?, ?);"
        try:
            cur=db.cursor()
            cur.execute(query, (name, address))
            db.commit()
            # print ("one record added successfully")
        except:
            print ("error in operation")
            db.rollback()

def read(id):    
    with db_connection() as db:        
        query = "SELECT * FROM Student WHERE Id=?;"
        cur = db.cursor()
        cur.execute(query, str(id))
        while True:
            record=cur.fetchone()
            if record == None:
                break
            print (record)

if __name__ == "__main__":
    # create() 
       
    for i in range(0, 10001, 1000):
        start = time.time()        
        insert("Alex", "LA")
        end = time.time()

        with open("results2.csv","a") as target:
            target.write("1" + "," + str(end - start) + "\n")

        time.sleep(1)
        start = time.time()
        for num in range(i):
            insert("Alex", "LA")
        end = time.time()
        
        with open("results2.csv","a") as target:
            target.write(str(i) + "," + str(end - start) + "\n")
        print(f"loop {i} end.")
        time.sleep(1)

    subprocess.run(["shutdown", "-h", "now"])

    # read(3)