# Learn Python in Arabic #132 -واجهات بايثون Python gui عنوان فورم label form tkinter Python in Arabic
import tkinter 
from  tkinter import ttk
frm = tkinter.Tk()
frm.geometry('600x400')
frm.title('Testing')
frm.config(background='#00affd')

#### label
lbl1 = ttk.Label(frm , text='lable 1 test',background='yellow')
lbl2 = ttk.Label(frm , text='lable 2 test')#, background='#660198')
lbl3 = ttk.Label(frm,text='Hallo')
lbl1.pack()
lbl2.pack()
lbl3.pack()

frm.mainloop()