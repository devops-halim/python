# Learn Python in Arabic #133 - gui لون عنوان فورم color label form tkinter Python in Arabic
import tkinter
from tkinter import ttk
frm = tkinter.Tk()
frm.geometry('600x400')
frm.config(background='#660198')
lbl1= ttk.Label(frm, text='Hallo')
lbl2 = ttk.Label(frm, text='Hi')

lbl1.pack()
lbl2.pack()
lbl1.config(background='navy',foreground='lightblue')

frm.mainloop()