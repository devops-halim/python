# Learn Python in Arabic #140 - Python gui برمجة الزر Command Button form tkinter Python in Arabic
def test():
    print('yes the button clicked')
import tkinter
from tkinter import ttk
backdroundcolor = 'lightblue'
frm = tkinter.Tk()
frm.title('test')
frm.geometry('800x600')
frm.config(background=backdroundcolor)

fnt= ('arial',20)
lblstyl = ttk.Style()
lblstyl.configure('TLabel', font=fnt,background=backdroundcolor)
btnstyle = ttk.Style()
btnstyle.configure('TButton', font=fnt)

lblname = ttk.Label(frm,text='Enter your name:',style='TLabel')
txtnme = ttk.Entry(frm,font=fnt)

lbladdress = ttk.Label(frm,text='Enter your adress:',style='TLabel')
txtaddress = ttk.Entry(frm,font=fnt)

btn = ttk.Button(frm,text='click me', state='TButton', command=test)

lblname.pack()
txtnme.pack()
lbladdress.pack()
txtaddress.pack()
btn.pack()
frm.mainloop()