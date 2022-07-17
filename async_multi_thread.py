"""this module explain multi threading.
   notice different t.start() and t.start()/t.join()
   t.start()          ---> async multithreading
   t.start()/t.join() ---> sync multithreading
   
Global Interpreter Lock (GIL)

The Global Interpreter Lock aka GIL was introduced to make CPython’s memory handling easier 
and to allow better integrations with C (for example the extensions). 
The GIL is a locking mechanism that the Python interpreter runs only one thread at a time. 
That is only one thread can execute Python byte code at any given time. 
This GIL makes sure that multiple threads DO NOT run in parallel.
Quick facts about the GIL:
    One thread can run at a time.
    The Python Interpreter switches between threads to allow concurrency.
    The GIL is only applicable to CPython (the defacto implementation). Other implementations like Jython, IronPython don’t have GIL.
    GIL makes single threaded programs fast.
    For I/O bound operations, GIL usually doesn’t harm much.
    GIL makes it easy to integrate non thread safe C libraries, thansk to the GIL, we have many high performance extensions/modules written in C.
    For CPU bound tasks, the interpreter checks between N ticks and switches threads. So one thread does not block others.
Many people see the GIL as a weakness. 
I see it as a blessing since it has made libraries like NumPy, 
SciPy possible which have taken Python an unique position in the scientific communities.
"""
#!/usr/bin/env python3

import threading
import time
import random

def worker(number):
    """
    function doc string
    """
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print(f"I am Worker {number}, I slept for {sleep} seconds")

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    # this is async multithreading
    # order of executing thraeds: t0, t4, t1, t3, t2 (may different every run)
    t.start()
    # this is sync multithreading
    # order of executing thraeds: t0, t1, t2, t3, t4
    # t.join()

print("All Threads are queued, let's see when they finish!")
