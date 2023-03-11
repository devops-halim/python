# Learn Python in Arabic #137 - gui مربع نص text box entry form tkinter Python in Arabic
import tkinter
from tkinter import ttk

frm= tkinter.Tk()
frm.geometry('700x500')
frm.title('Testing')
#frm.config(background='#ffffff')

lbl1 = ttk.Label(frm,text='Enter youre name')
txt = ttk.Entry(frm)
font1= ('consolas',40)
lbl1.config(font=font1)
txt.config(font=font1)

lbl1.pack()
txt.pack()

frm.mainloop()
