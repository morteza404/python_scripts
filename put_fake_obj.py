#!/usr/bin/env python3

import requests
import time
import random

TS = time.time()

PUT_NUMBER = 1000

def put(step):
    for _ in range(1,step):
        headers = {
                        "X-Timestamp": str(TS),
                        "Accept-Encoding": "identity",
                        "X-Content-Type": "application/octet-stream",
                        "X-Size": "35",
                        "X-Etag": "f2e6121b3f1ada44e881396e93ada62d"
                    }
        url = "http://192.168.122.9:6221/sdb2/509/AUTH_test/c1/new_901_fake_object_"+ str(random.random())

        requests.put(url=url, headers = headers)

if __name__ == "__main__":

    start = time.time()
    
    put(PUT_NUMBER)

    end = time.time()

    print(f"time = {end - start}")   

    print("OK")