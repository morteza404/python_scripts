from time import time
from threading import Thread
from multiprocessing import Process



def count_down(n):
    while n > 0:
        n -= 1

# before = time()
# thread1 = Thread(target=count_down, args=(100000000,))
# thread2 = Thread(target=count_down, args=(100000000,))
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# after = time()
# print(after-before)

before = time()
process1 = Process(target=count_down, args=(100000000,))
process2 = Process(target=count_down, args=(100000000,))
process1.start()
process2.start()
process1.join()
process2.join()
after = time()
print(after-before)