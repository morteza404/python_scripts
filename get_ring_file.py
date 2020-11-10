import requests
import base58
import base64
import json
import os

RING_LIST = ["object.builder", "container.builder", "account.builder", "object.ring.gz", "container.ring.gz", "account.ring.gz",]
NEW_PATH = os.environ.get('RINGS_PATH', "/home/shahbazi/Desktop/new_rings/")
TENDERMINT_BASE_URL = "http://localhost:26657"

def get_trx():
    for i in RING_LIST:
        res = requests.get(f'{TENDERMINT_BASE_URL}/abci_query?data="{i}"')
        # print(res.text)
        trx_value = json.loads(res.text)["result"]["response"]["value"]
        b64_value = base64.standard_b64decode(trx_value)
        b64_list = str(b64_value).split('b"b')[1].replace('"','').replace('\'','')
        b64_bytes = bytes(b64_list, 'utf-8') 
        # print(base58.b58decode(b64_bytes))
        with open(NEW_PATH + i,"wb") as file:
            file.write(base58.b58decode(b64_bytes))
    print("DONE!!!")

if __name__ == "__main__":
    get_trx()