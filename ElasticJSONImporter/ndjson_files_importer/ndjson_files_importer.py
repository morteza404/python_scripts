from elasticsearch import helpers, Elasticsearch
import ndjson
import time
import os

es = Elasticsearch(['localhost'], port=9200)

start = time.time()
for filename in os.listdir():
    if filename.endswith(".ndjson"):
        f = open(filename)
        docket_content = f.read()
        data=ndjson.loads(docket_content)
        # Send the data into es
        if es.indices.exists(index=f.name[:-7]):
                print(f"`{f.name}` index allready exists.")
        else:
                helpers.bulk(es, data, index=f.name[:-7])
                end = time.time()
                print(f"`{f.name}` indexed in {end - start} seconds successfully.")
        
 
        

         
        
    
    





















