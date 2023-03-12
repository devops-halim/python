from tkinter import *
frm = Tk()
frm.geometry('900x600')

def button7(seiben):
    str7.set(seiben)
str7 = IntVar()
Label(frm,textvariable=str7).pack()
Button(frm,text='7',command=lambda:button7('7')).pack()
Button(frm,text='8',command=lambda:button7('8')).pack()
Button(frm,text='9',command=lambda:button7('9')).pack()
frm.mainloop()