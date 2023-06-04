# Learn Python in Arabic #176 - gui تلوين الشاشة و الادوات bg all controls tkinter Python in Arabic
from tkinter import *
from tkinter import ttk
from tools import *

frm = Tk()
frm.geometry('700x600')
tkcnter(frm)
Label(frm,text='lbl1').pack()
Entry(frm).pack()
Button(frm,text='OK').pack()
ttk.Button(frm,text='yes').pack()
ttk.Entry(frm).pack()
ttk.Label(frm,text='ttk lbl1').pack()



backgroundall(frm,'lightblue')




frm.mainloop()