# Learn Python in Arabic #138 - Python gui نمط و شكل style form tkinter Python in Arabic
import tkinter
from tkinter import ttk

frm = tkinter.Tk()
frm.title('test')
frm.geometry('800x600')
frm.config(background='pink')

fnt= ('arial',20)
lblstyl = ttk.Style()
lblstyl.configure('TLabel', font=fnt,background='#00ffff')

lblname = ttk.Label(frm,text='Enter your name:',style='TLabel')
txtnme = ttk.Entry(frm,font=fnt)

lbladdress = ttk.Label(frm,text='Enter your adress:',style='TLabel')
txtaddress = ttk.Entry(frm,font=fnt)

lblname.pack()
txtnme.pack()
lbladdress.pack()
txtaddress.pack()
frm.mainloop()