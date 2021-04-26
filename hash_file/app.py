#!/usr/bin/env python3

from decorators import calc_time
import hashlib

"""
    BLOCK_SIZE = 65536 # The size of each read from the file.
"""

@calc_time
def hash_file(file_name, BLOCK_SIZE):
    file_hash = hashlib.sha256() 
    with open(file_name, 'rb') as f: 
        fb = f.read(BLOCK_SIZE) 
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file

    print(f"the file {file_name} hash is : {file_hash.hexdigest()}") # Get the hexadecimal digest of the hash

hash_file("../Swift_CAS_zblock.pdf", 65536)