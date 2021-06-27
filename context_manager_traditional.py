
# Creating context managers the traditional way, by writing a class with __enter__() and __exit__() methods.
class SampleContextManager:
    def __enter__(self):
        print('---> Entered into context manager!')

    # def __exit__(self, exc_type, exc_value, traceback)
    def __exit__(self, *args):
        print('<--- Exiting from context manager!')


with SampleContextManager():
    print('Inside context manager!')
