from threading import Thread

def task1():
	print([i for i in range(20) if i%2 == 0])
	
def task2():
	print([i for i in range(20) if i%2 == 1])	
		
thread1 = Thread(target = task1)

thread2 = Thread(target = task2)

thread1.start()

thread2.start()