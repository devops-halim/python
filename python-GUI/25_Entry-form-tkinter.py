# Learn Python in Arabic #146 -واجهات بايثون Python gui نص افتراضي Entry form tkinter Python in Arabic
from tkinter import *

frm = Tk()
frm.geometry('700x500')
Label(frm,text='lbl test',bg='navy',fg='lightblue',font='arial 45 underline').pack()

stringvarname = StringVar()
txt = Entry(frm,bg='yellow',fg='blue',font='tahoma 30 bold',textvariable=stringvarname)
stringvarname.set('enter your name')

txt.pack()
frm.mainloop()