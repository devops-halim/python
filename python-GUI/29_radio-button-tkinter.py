# Learn Python in Arabic #150 -واجهات Python gui اختيار الراديو radio button tkinter Python in Arabic
from tkinter import *
frm = Tk()
frm.geometry('900x600')
v =IntVar()
rdom = Radiobutton(frm,text='male',value=1,variable=v)
rdof= Radiobutton(frm,text='female',value=2,variable=v)
rdom.pack()
rdof.pack()

strvar =StringVar()
strvar.set('yes')
rdoyes = Radiobutton(frm,text='yes',value='yes',variable=strvar)
rdono= Radiobutton(frm,text='no',value='no',variable=strvar)
rdoyes.pack()
rdono.pack()

def prf():
    print(v.get())

def prfyesno():
    print(strvar.get())
Button(frm,text='OK',command=prf).pack()
Button(frm,text='click',command=prfyesno).pack()

frm.mainloop()