# Learn Python in Arabic #173 - gui اخفاء و اظهار الادوات hide show control tkinter Python in Arabic
from tkinter import *
import tools

frm = Tk()
frm.geometry('600x400')
tools.tkcnter(frm)


lbl1 = Label(frm,text='Welcome To TK',font='None 30 bold')
lbl1.pack()

def hide():
    lbl1.pack_forget()

def show():
    lbl1.pack()

Button(frm,text='hide',font='None 30 bold',command=hide).pack()
Button(frm,text='show',font='None 30 bold',command=show).pack()

frm.mainloop()