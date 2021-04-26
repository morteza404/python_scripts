from pathlib import Path
from elasticsearch import helpers, Elasticsearch
import ndjson
import time

es = Elasticsearch(['localhost'], port=9200)

f = Path("generated.ndjson", errors="ignore").read_text()

data = ndjson.loads(f)

start = time.time()

helpers.bulk(es, data, index='generated')

end = time.time()

print('json file index successfully.')





