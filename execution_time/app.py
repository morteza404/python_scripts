import timeit
# import_module = "import random"
# testcode = ''' 
# def test(): 
#     return random.randint(10, 100)
# '''

testcode = """
def test(): 
    return "hello"
           """

# print(timeit.repeat(stmt=testcode, setup=import_module, repeat=10))

print(timeit.repeat(stmt=testcode, repeat=1))