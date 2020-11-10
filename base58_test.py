import requests
import base58
import base64
import json

with open("/home/shahbazi/Desktop/object.builder","rb") as file:
    s = file.read()
    # print(s)

k5 = "file10"

v5 = base58.b58encode(s)

##### get value #####
res = requests.get(f'http://172.17.0.2:26657/abci_query?data="{k5}"')
# print(res.text)

##### send binary file as trx #####
# res = requests.get(f'http://172.17.0.2:26657/broadcast_tx_commit?tx="{k5}={v5}"')
# print(res.text)

dd = json.loads(res.text)["result"]["response"]["value"]

# print(dd)

# ff = base64.b64decode(dd)

ff = base64.standard_b64decode(dd)

ff_list = str(ff).split('b"b')[1].replace('"','').replace('\'','')
ff_bytes = bytes(ff_list, 'utf-8') #bytes(mystring, 'utf-8')
print(ff_list)
#ff = base64.standard_b64decode(ff_list)

print(base58.b58decode(ff_bytes))




