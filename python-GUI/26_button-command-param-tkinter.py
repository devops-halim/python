from tkinter import *

frm = Tk()
frm.geometry('700x500')
Label(frm,text='lbl test',bg='navy',fg='lightblue',font='arial 45 underline').pack()

stringvarname = StringVar()
txt = Entry(frm,bg='yellow',fg='blue',font='tahoma 30 bold',textvariable=stringvarname)
stringvarname.set('enter your name')
txt.pack()

def test():
    stringvarname.set('hallo')

def test2(anyword):
    stringvarname.set(anyword)

Button(frm,text='OK',background='darkred',foreground='pink',font='arial 30',command=test) .pack()
Button(frm,text='OK',background='pink',foreground='darkred',font='arial 30',command=lambda:test2('hey')) .pack()


frm.mainloop()