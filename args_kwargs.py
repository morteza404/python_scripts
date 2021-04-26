def f(*args):
    print(sum(args))

f(10)

f(10,20)

f(10,20,30)


def myFun(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
   
myFun("Hi", first ='Geeks', mid ='for', last='Geeks') 