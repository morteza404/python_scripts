from contextlib import contextmanager

# Creating a Context Manager the new way, by using generatoer.
# generator is method that uses yield instead of return
# before yield call __enter__ & after yield call __exit__
@contextmanager
def show_message():
    print("------> enter to ctx manager")
    try:        
        # yield {}
        yield True
    finally:
        print("<------ exit fron ctx manager")


with show_message():
    print("hello ctx manager !@!")