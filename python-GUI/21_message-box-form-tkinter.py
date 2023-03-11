# Learn Python in Arabic #142 - gui صندوق رسالة message box form tkinter Python in Arabic
from tkinter import messagebox
import tkinter
from tkinter import ttk
bg = '#f0f0ff'
frm=tkinter.Tk()
frm.title('test')
frm.geometry('600x300')
frm.config(background=bg)

fnt = ('arial',25)
lblstyl=ttk.Style()
lblstyl.configure('TLabel', font=fnt) # TLabel

lblname = ttk.Label(frm,text='Enter your name: ',style='TLabel')
txt = ttk.Entry(frm,font=fnt)

def sayhallo():
    messagebox.showinfo('Welcome', 'Hallo'+' '+ txt.get())
    #messagebox.showerror('404')
    #messagebox.showwarning('500')
    
btnstyl = ttk.Style()
btnstyl.configure('TButton', font=fnt)
btn = ttk.Button(frm,text='click me',style='TButton',command=sayhallo)

lblname.pack()
txt.pack()
btn.pack()
frm.mainloop()