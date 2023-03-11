# Learn Python in Arabic #136 - gui الحشو عنوان padding label form tkinter Python in Arabic
from tkinter import ttk
import tkinter
frm = tkinter.Tk()

frm.geometry('700x500')

lbl1=ttk.Label(frm,text='Test')
lbl2=ttk.Label(frm,text='test2')
lbl3=ttk.Label(frm,text='test3')
lbl4=ttk.Label(frm,text='test4')
lbl5=ttk.Label(frm,text='test5')

lbl1.config(background='navy',foreground='lightblue')
lbl1.config(font=('arial',40),padding=30)

lbl2.config(background='black',foreground='pink')
lbl2.config(font=('thoma',30),padding=20)

lbl3.config(background='black',foreground='red')
lbl3.config(font=('arial',15),padding=(20,15))

lbl4.config(background='red',foreground='lightblue')
lbl4.config(font=('arial',15),padding=(40,70))

lbl5.config(background='orange',foreground='black')
lbl5.config(font=('arial',15),padding=(20,30,40,50))

lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
lbl5.pack()
frm.mainloop()