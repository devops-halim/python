# Learn Python in Arabic #135 - gui حجم خط عنوان font size label form tkinter Python in Arabic
import tkinter
from tkinter import ttk

frm = tkinter.Tk()
frm.geometry('700x500')
frm.title('hi')

lbl1= ttk.Label(frm,text="Welcome back")
lbl2 = ttk.Label(frm,text='Hi')
lbl3 = ttk.Label(frm,text='Yes/NO')

lbl1.config(background='darkred', font=('arial',48), foreground='pink')
lbl2.config(background='darkblue', font=('arial',25), foreground='pink')
lbl3.config(background='black', font=('arial',100), foreground='pink')

lbl1.pack()
lbl2.pack()
lbl3.pack()
frm.mainloop()