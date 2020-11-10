"""
Pickling: the Concept
Suppose you just spent a better part of your afternoon working in Python, processing many data sources to build an elaborate, highly structured data object. Say it is a dictionary of English words with their frequency counts, translation into other languages, etc. And now it's time to close your Python program and go eat dinner. Obviously you want to save this object for future use, but how?

You *could* write the data object out to a text file, but that's not optimal. Once written as a text file, it is a simple text file, meaning next time you read it in you will have parse the text and process it back to your original data structure.

What you want, then, is a way to save your Python data object as itself, so that next time you need it you can simply load it up and get your original object back. Pickling and unpickling let you do that. A Python data object can be "pickled" as itself, which then can be directly loaded ("unpickled") as such at a later point; the process is also known as "object serialization".
How to Pickle/Unpickle
Pickling functions are part of the pickle module. You will first need to import it. And, pickling/unpickling obviously involves file IO, so you will have to use the file writing/reading routines you learned in the previous tutorial.

"""

import pickle
import os

path = os.environ.get("HOME")


# pickling

pickled_data = {"name":"morteza","city":"hamedan"}
with open(path + "/test.pkl","wb") as pickle_file:
    pickle.dump(pickled_data, pickle_file)
print("done")

# unpickling

with open(path + "/test.pkl","rb") as pickle_file:
    unpickled_data = pickle.load(pickle_file)
print(unpickled_data)

