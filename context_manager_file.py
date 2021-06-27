from contextlib import contextmanager

@contextmanager
def context():
    with open("context.txt", "w") as target:
        target.write("----> enter to ctx manager\n")
    try:
        yield True
    finally:
        with open("context.txt", "a") as target:
            target.write("<---- exit from ctx manager\n")

with context():
    with open("context.txt", "a") as target:
        target.write("ctx manager\n")
    print("done")
