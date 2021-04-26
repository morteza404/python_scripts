from multiprocessing import Process

def f(name):
    print('hello ', name)

if __name__ == '__main__':
    for i in range(10):
        Process(target=f, args=('bob',)).start()
        #p = Process(target=f, args=('bob',))
        #p.start()
        #p.join()
