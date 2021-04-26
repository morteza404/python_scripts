#-*- coding= utf-8 -*-
#In The Name Of God

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

class W_F:
    def r_s(self):
        #Root Settings
        self.root = Tk()
        self.root.config(background='Black')
        self.root.resizable(False,False)
        self.root.geometry('500x200+400+235')
        self.root.title('word mirror finder')

    def lbf(self):
        #Labels - Buttons - Fields(Entry)
        self.label1 = ttk.Label(self.root,
                                text='< Welcome >',
                                background='Black',
                                foreground='White')
        self.label2 = ttk.Label(self.root,
                                text='Word : ',
                                background='Black',
                                foreground='White')
        self.field1 = ttk.Entry(self.root,
                                width=40)
        self.button1 = ttk.Button(self.root,
                                  text='Check')
        self.button2 = ttk.Button(self.root,
                                  text='Exit')

    def p(self):
        #place of l,b,s
        self.label1.config(font=('Vazir',20))
        self.label1.place(x=155 ,y=10)
        self.label2.config(font=('Vazir',15))
        self.label2.place(x=10 ,y=100)
        self.field1.place(x=77 ,y=104)
        self.button1.place(x=340 ,y=102)
        self.button2.place(x=415, y=170)

    def bs(self):
        #Buttons Style
        style = ttk.Style()
        style.configure('TButton',
                        foreground='Blue')

    def bc(self):
        #Button Commands
        def c_b():
            #Check Button Command
            self.Field1_Word = self.field1.get()
            if (self.Field1_Word == ''):
                messagebox.showinfo(title='Checked', message=';/')
            elif (self.Field1_Word == self.Field1_Word[::-1]):
                messagebox.showinfo(title='Checked', message='<  True  >')
            else:
                messagebox.showinfo(title='Checked', message='</  False  >')
        self.button1.config(command=c_b)
        def e_b():
            #Exit Button Command
            a_e = messagebox.askyesno(title='Exit?', message='<WARNING>  Are You Sure To Exit ?  </WARNING>')
            if a_e == True:
                sys.exit()
        self.button2.config(command=e_b)

if __name__ == '__main__':
    Word_Mirror_Finder = W_F()
    Word_Mirror_Finder.r_s()
    Word_Mirror_Finder.lbf()
    Word_Mirror_Finder.p()
    Word_Mirror_Finder.bs()
    Word_Mirror_Finder.bc()
    Word_Mirror_Finder.root.mainloop()
