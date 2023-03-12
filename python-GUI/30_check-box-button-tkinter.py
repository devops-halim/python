# Learn Python in Arabic #151 - Python gui صندوق اختيار check box button tkinter Python in Arabic
from tkinter import *

frm = Tk()
frm.geometry('900x700')
v = IntVar()
chbut = Checkbutton(frm,text='ok', variable=v)
chbut.pack()

def f():
    print(v.get())
Button(frm,text='ok',command=f).pack()

v1 = BooleanVar()
chbut1 = Checkbutton(frm,text='ok', variable=v1)
chbut1.pack()


def f1():
    print(v1.get())
Button(frm,text='check',command=f1).pack()




frm.mainloop()