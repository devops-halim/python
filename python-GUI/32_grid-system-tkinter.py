# Learn Python in Arabic #154 - Python gui نظام الجريد grid system tkinter Python in Arabic

from tkinter import *
frm = Tk()
frm.geometry('900x700')
lbl = Label(frm,text='btn1',font='arial 25 bold')
btn = Button(frm,text='btn1',font='arial 25 bold')


lbl2 = Label(frm,text='btn2',font='arial 25 bold')
btn2 = Button(frm,text='btn2',font='arial 25 bold')

lbl3 = Label(frm,text='btn3',font='arial 25 bold')
btn3 = Button(frm,text='btn3',font='arial 25 bold')

lbl4 = Label(frm,text='btn4',font='arial 25 bold')
btn4 = Button(frm,text='btn4',font='arial 25 bold')

lbl.grid(row=0,column=0)
btn.grid(row=0,column=1)

lbl2.grid(row=1,column=0)
btn2.grid(row=1,column=1)

lbl3.grid(row=3,column=1)
btn3.grid(row=3,column=2)

lbl4.grid(row=4,column=7)
btn4.grid(row=9,column=6)

frm.mainloop()