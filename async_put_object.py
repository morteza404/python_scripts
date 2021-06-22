#!/usr/bin/env python3

import asyncio
import time
import aiohttp
import random

TS = time.time()

STEP = 10000

headers = {
            "X-Timestamp": str(TS),
            "Accept-Encoding": "identity",
            "X-Content-Type": "application/octet-stream",
            "X-Size": "35",
            "X-Etag": "f2e6121b3f1ada44e881396e93ada62d"
          }

url = "http://192.168.1.192:6201/sda1/95/AUTH_test/c1/new_901_fake_object_"+ str(random.random())


async def put():
    async with aiohttp.ClientSession() as session:
        for _ in range(1,STEP):
            await session.put(url=url, headers=headers)       
    

if __name__ == "__main__":

    start = time.time()    
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(put_many())
    asyncio.run(put())
    end = time.time()
    print(f"time taken = {end - start} seconds.")   
