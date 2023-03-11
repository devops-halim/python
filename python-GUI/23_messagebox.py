from tkinter import ttk
import tkinter
from tkinter import messagebox


frm = tkinter.Tk()
frm.title('messgbox')
frm.geometry('600x300')
fnt =('arial',50)
btnstyl = ttk.Style()
btnstyl.configure('TButton',font=fnt)
def error():
    tkinter.messagebox.askokcancel('hallo','404')
    messagebox.askquestion('hallo','404')
    messagebox.askretrycancel('hi','404 not found')
    messagebox.askyesno()
    messagebox.askyesnocancel()

btn = ttk.Button(frm,text='ok',command=error,style='TButton',padding='10')

btn.pack()

frm.mainloop()