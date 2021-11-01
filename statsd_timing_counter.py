#!/usr/bin/env python3

import statsd

c = statsd.StatsClient("127.0.0.1", port=8125, prefix="swift_test")

size = 0
for _ in range(1,100000):  
    c.incr("put_count")
    size += 500
    c.timing("put_size", size) 

print("finish")       
