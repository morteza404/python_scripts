import hashlib
import time

name = "simpletext"

nonce = 1

start = time.time()

while True: 
   
    data = name + "-" + str(nonce)

    hash = hashlib.sha256(data.encode()).hexdigest()

    if hash[:4] != "0000":        
        nonce += 1

    else:
        print(f"name-nonce is : {data}")
        print(f"hash is : {hash}")
        break     
        
end = time.time()

print(f"completed in {(end - start) // 1000} Sec")


    
