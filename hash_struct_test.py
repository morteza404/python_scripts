import hashlib
import struct

hashobj = hashlib.md5("mom.png".encode()).hexdigest()

print(hashobj)

# int(obj, 16) : convert hex to decimal 
print(int(hashobj,16))
print(int(hashobj,16) % 25)



# for bit operation (like shift) we need struct
data = struct.unpack_from(">I", hashobj)[0]
print(data)
print(data >> 2)