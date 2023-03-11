# Learn Python in Arabic #148 -واجهات بايثون Python gui قائمة منسدلة combobox tkinter Python in Arabic
from tkinter import ttk
import tkinter

frm = tkinter.Tk()
frm.geometry('600x400')

cbx1 = ttk.Combobox(frm,values=('Gera','jena' ,'erfurt','Leipzig'))
cbx1.current(3)
cbx2 = ttk.Combobox(frm,values=('Gera','jena' ,'erfurt','Leipzig'),state='readonly') # readonly

def printcbx():
    print(cbx1.get())

btn1 = ttk.Button(text='OK',command=printcbx)

cbx1.pack()
cbx2.pack()
btn1.pack()
frm.mainloop()