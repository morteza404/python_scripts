from elasticsearch import helpers, Elasticsearch
import json

es = Elasticsearch(['localhost'], port=9200)

with open("imagenet_class_index.json") as file:
	docs = json.load(file)
	helpers.bulk(es, docs, index='image')
			
print('json file index successfully.')