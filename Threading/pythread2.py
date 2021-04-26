from threading import Thread

def f1():
    print('morteza')

def f2():
    print('shahbazi')

def f3():
    print('jalali')    


for item in range(1000000000):

    thread1 = Thread(target=f1)

    thread2 = Thread(target=f2) 

    thread3 = Thread(target=f3) 

    thread1.start() 

    thread2.start()

    thread3.start()            