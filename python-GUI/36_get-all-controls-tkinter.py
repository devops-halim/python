# Learn Python in Arabic #174 - Python gui جميع ادوات الفورم get all controls tkinter Python in Arabic

from tkinter import *
from tkinter import ttk
import tools

frm = Tk()
frm.geometry('600x400')
tools.tkcnter(frm)
Label(frm,text='labl 1').pack()
Label(frm,text='labl 2').pack()
Label(frm,text='labl 3').pack()
Label(frm,text='labl 4').pack()
Label(frm,text='labl 5').pack()
Button(frm,text='ok').pack()
Listbox(frm).pack()
Entry(frm).pack()

ttk.Label(frm,text='labl 1').pack()
ttk.Label(frm,text='labl 2').pack()
ttk.Label(frm,text='labl 3').pack()
ttk.Label(frm,text='labl 4').pack()
ttk.Label(frm,text='labl 5').pack()
ttk.Button(frm,text='ok').pack()
ttk.Entry(frm).pack()

controls = frm.winfo_children()
for c in controls:
    print(c)
    print ('______________')
    print(type(c))
    print ('______________')
    print(type(c).__name__)

frm.mainloop()