n = int(input('enter a number : '))
def fibo(n):
	if(n<=1):
		return 1
	else:
		return fibo(n-1)+fibo(n-2)
		
print('fibo',n ,'is:', fibo(n))		
		
		