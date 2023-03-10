# Learn Python in Arabic #134 - gui خط عنوان فورم font label form tkinter Python in Arabic
import tkinter
from tkinter import ttk

frm = tkinter.Tk()
frm.title("Hi")
frm.geometry('700x500')
lbl1= ttk.Label(frm,text='test')
lbl2 = ttk.Label(frm,text='test 2')
lbl3 = ttk.Label(frm,text='test 3')

lbl1.pack()
lbl2.pack()
lbl3.pack()
# arial , tahoma , impact
lbl1.config(background='navy',foreground='lightblue',font='impact')
frm.mainloop()