import time
import threading
import mmap

with open('f.txt', 'rb') as f1:
# Size 0 will read the ENTIRE file into memory!
	f = mmap.mmap(f1.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only
#f = open("f.txt", "r")


def task1(x):
	while True:
		line = f.readline()
		if line == b'':
			#print("break",len(line))
			break
		print(line)
		print ("task1-current time : ",time.ctime())
		time.sleep(6)

def task2(x):
	while True:
		line = f.readline()
		if line == b'':
			break
		print(line)
		print ("task2-current time : ",time.ctime())
		time.sleep(3)

p = 5

t1 = threading.Thread(target=task1, args=(p,))
t2 = threading.Thread(target=task2, args=(p,))


t1.start()
print("t1.start()")
t2.start()
print("t2.start()")

t2.join()
print("t2.join()")
t1.join()
print("t1.join()")

f.close()

print("Done!")
