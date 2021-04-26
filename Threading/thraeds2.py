from threading import Thread

def func(i):
    print('thread {} is running.'.format(i))

threads = []

for i in range(500):
    t = Thread(target=func, args=(i,))
    threads.append(t)
    t.start()
    t.join()
