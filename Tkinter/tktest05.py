from tkinter import *
from tkinter import filedialog

root = Tk()

root.fileName = filedialog.askopenfilename(('how files' , '.xlsx'), ('all files', '*.*'))

root.mainloop()
