from tkinter import *

root = Tk()

root.title('Hello')

lbl = Label(root, text='First App.').pack()

btn = Button(root, text='Exit', command= root.destroy).pack()

root.mainloop()