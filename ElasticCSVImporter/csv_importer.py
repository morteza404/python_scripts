from pathlib import Path
from elasticsearch import helpers, Elasticsearch
import csv
import time

es = Elasticsearch(['localhost'], port=9200)

csvfile = Path("bbc-text.csv", errors="ignore")

start = time.time()

with open('bbc-text.csv') as file:
	reader = csv.DictReader(file)
	helpers.bulk(es, reader, index=csvfile.name[:-4])

end = time.time()

print(f"{csvfile.name} file index successfully in {end - start} seconds.")



