import tkinter
from tkinter import ttk

frm= tkinter.Tk()
frm.title('Calculater')
frm.geometry('450x250')

fnt = ('arial 20 bold')

lblnum1 = ttk.Label(frm,text='Num 1 :',font=fnt)
lblnum2 = ttk.Label(frm,text='Num 2 :',font=fnt)

svnum1 = tkinter.StringVar()
svnum2 = tkinter.StringVar()
svnum1.set('1')
svnum2.set('2')
txtnum1 = ttk.Entry(frm,font=fnt,textvariable=svnum1)
txtnum2 = ttk.Entry(frm,font=fnt,textvariable=svnum2)

lblnum1.grid(row=0,column=0,pady=10,padx=10)
txtnum1.grid(row=0,column=1,pady=10,padx=10)
lblnum2.grid(row=1,column=0)
txtnum2.grid(row=1,column=1)

def calc(ope):
    strn1 = str(txtnum1.get())
    strn2 = str(txtnum2.get())
    n1 = int(strn1)
    n2 = int(strn2)
    r = 0
    if ope == '+': r = n1+n2
    elif ope == '-': r=n1-n2
    elif ope =='x':r = n1*n2
    else:
        if n2 ==0:n2=1
        r = n1/n2
    lblerg['text']=('Result: %s %s %s = %s' %(n1,ope,n2,round(r,3)))
btnstyl = ttk.Style()
btnstyl.configure('TButton',font=fnt,padding=10)

frmaes = tkinter.Frame(frm)

btn_width = 5
btn_plus = ttk.Button(frmaes,text='+',width=btn_width,command=lambda:calc('+'))
btn_sub = ttk.Button(frmaes,text='-',width=btn_width,command=lambda:calc('-'))
btn_mul = ttk.Button(frmaes,text='x',width=btn_width,command=lambda:calc('x'))
btn_div = ttk.Button(frmaes,text='/',width=btn_width,command=lambda:calc('/'))

frmaes.grid(row=2,column=0,columnspan=2)
btn_plus.grid(row=0,column=0)
btn_sub.grid(row=0,column=1)
btn_mul.grid(row=0,column=2)
btn_div.grid(row=0,column=3)

lblerg = ttk.Label(frmaes,text='Result:',font=fnt)
lblerg.grid(row=1,column=0,columnspan=4)

frm.mainloop()