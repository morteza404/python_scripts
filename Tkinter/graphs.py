from tkinter import *

root = Tk()

root.title('Morteza')

lbl = Label(root, text='Salam').pack()

btn = Button(root, text='Exit', command=root.destroy).pack()

root.mainloop()