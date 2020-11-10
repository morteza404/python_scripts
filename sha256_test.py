# import hashlib

# data = ["ali","reza","hassan","saeid"]

# nonce = 1000

# while True:    

#     for item in data:

#         item += str(nonce)

#         hash = hashlib.sha256(item.encode()).hexdigest()

#         if hash[-4:] == "1111":
#             print(item, hash)
#             nonce += 1

#         break    

import hashlib
import time

name = "ali"

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


    