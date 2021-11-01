from tqdm import tqdm
import sqlite3
  
for i in tqdm (range (100), desc="Loading..."):
    try:
        with sqlite3.connect("44880a2b3cb827bc888b15d0add13083.db") as db:
            query = "select name from object;"
            cur = db.cursor()
            cur.execute(query)
            data = cur.fetchall()
            # with open("test.txt", "w") as f:
            #     f.write(str(data))
    except sqlite3.Error as error:
        print("Error while connecting a sqlite db:\n", error)
        
		