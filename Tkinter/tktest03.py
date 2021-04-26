from tkinter import *
#import tkFileDialog
from tkinter import filedialog
import csv

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        self.menuBar = Menu(top)
        top["menu"] = self.menuBar
        self.subMenu = Menu(self.menuBar)
        self.menuBar.add_cascade(label = "File", menu = self.subMenu)
        self.subMenu.add_command( label = "Read Data",command = self.readCSV)


    def readCSV(self):
        self.filename = filedialog.askopenfilename()
        f = open(self.filename,"rb")
        read = csv.reader(f, delimiter = ",")
        #buttons = read.next()
        print()
##        for btn in buttons:
##            new_btn = Button(self, text=btn, command=self.btnClick)
##            new_btn.pack()

    def btnClick(self):
        pass

app = Application()
app.master.title("test")
app.mainloop()
