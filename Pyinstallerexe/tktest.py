from tkinter import *
root = Tk()
root.title("Morteza app")
root.geometry('350x200')
lbl = Label(root, text="Hello")
# lbl.grid(column=2, row=0)
lbl.pack()
def clicked():
    lbl.configure(text="Fucking Jalali !!")
btn = Button(root, text="Click Me", command=clicked)
# btn.grid(column=2, row=1)
btn.pack()
root.mainloop()