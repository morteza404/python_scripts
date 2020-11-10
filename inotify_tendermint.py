import inotify.adapters
import requests
import base58
import base64
import json

PATH = "/home/shahbazi/Desktop/rings/"
# NEW_PATH = "/home/shahbazi/Desktop/rings2/"
# RING_LIST = ["object.builder", "container.builder", "account.builder", "object.ring.gz", "container.ring.gz", "account.ring.gz",]

def notify(path):
    flag = False
    i = inotify.adapters.Inotify()
    i.add_watch(path)        
    try:
        for event in i.event_gen(yield_nones=False):
            (_, type_names, path, filename) = event
            #print (type_names)
            # print (type(filename))
            if "IN_MODIFY" in type_names:
                flag = True
            if (flag and "IN_CLOSE_WRITE" in type_names)  or ("IN_MOVED_TO" in type_names) :
                # print(f"PATH=[{path}] FILENAME=[{filename}] EVENT_TYPES={type_names}") 
                # print("salam :)")
                send_transaction(filename,filename)
                # get_transaction_value(filename,filename) 
            if (flag and "IN_CLOSE_WRITE" in type_names):
                flag = False       
                         
    except KeyboardInterrupt:
        pass
    finally:
        i.remove_watch(path)

def send_transaction(trx_key, ring_file):
    with open(PATH + ring_file,"rb") as file:    
        s = file.read()
        # print(s)
    trx_value = base58.b58encode(s)
    res = requests.get(f'http://172.17.0.2:26657/broadcast_tx_commit?tx="{trx_key}={trx_value}"')
    print(res.text)
    # global NEW_TRX
    # NEW_TRX = True

# trx_key : arbitrary transaction key name
# def get_transaction_value(trx_key):
#     res = requests.get(f'http://172.17.0.2:26657/abci_query?data="{trx_key}"')
#     # print(res.text)
#     trx_value = json.loads(res.text)["result"]["response"]["value"]
#     b64_value = base64.standard_b64decode(trx_value)
#     b64_list = str(b64_value).split('b"b')[1].replace('"','').replace('\'','')
#     b64_bytes = bytes(b64_list, 'utf-8') 
#     print(base58.b58decode(b64_bytes))
#     with open(NEW_PATH + f"{trx_key}","wb") as file:
#         file.write(base58.b58decode(b64_bytes))

# def get_trx():
#     for i in RING_LIST:
#         res = requests.get(f'http://172.17.0.2:26657/abci_query?data="{i}"')
#         # print(res.text)
#         trx_value = json.loads(res.text)["result"]["response"]["value"]
#         b64_value = base64.standard_b64decode(trx_value)
#         b64_list = str(b64_value).split('b"b')[1].replace('"','').replace('\'','')
#         b64_bytes = bytes(b64_list, 'utf-8') 
#         # print(base58.b58decode(b64_bytes))
#         with open(NEW_PATH + i,"wb") as file:
#             file.write(base58.b58decode(b64_bytes))
#     print("DONE!!!")

if __name__ == "__main__":
    print("start sending transaction...")
    notify(PATH)
    # get_trx()   
    