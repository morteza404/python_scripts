import os
for filename in os.listdir():
    os.rename(filename, filename.replace('_Downloadly.ir', ''))