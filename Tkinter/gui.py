import tkinter as tk

root = tk.Tk()

root.title('Test')

lbl = tk.Label(root, text='Hello World :)').pack()

btn = tk.Button(root, text='Exit', command = root.destroy).pack()

root.mainloop()