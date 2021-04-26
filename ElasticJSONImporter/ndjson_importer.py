from pathlib import Path
from elasticsearch import helpers, Elasticsearch
import ndjson
import time

es = Elasticsearch(['localhost'], port=9200)

ndfile = Path("generated.ndjson", errors="ignore")

data = ndjson.loads(ndfile.read_text())

start = time.time()

helpers.bulk(es, data, index=ndfile.name[:-7])

end = time.time()

print(f"{ndfile.name} file index in {end - start} seconds successfully.")





