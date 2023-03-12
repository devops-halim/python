from tkinter import *
from tkinter import ttk
from tkinter import messagebox

frm = Tk()
fnt = ('arial 25 bold')
bg = '#99C9FF'
bgtxt = '#ffffff'
fg = '#000000'
frmwidth = 800
frmhight = 600
x = (frm.winfo_screenwidth()-frmwidth) /2
y = (frm.winfo_screenheight()-frmhight)/2
pad = 10

frm.geometry('%dx%d+%d+%d'%(frmhight,frmhight,x,y))
frm.title('Employee Data Entry')
frm.config(background=bg)

Label(frm,text='Employee Data',background='#85BDDE',foreground='#142249',font=fnt).pack(pady=pad)
frame = Frame(frm,background=bg)
frame.pack(pady=pad)

Label(frame,text='ID:',background=bg,foreground=fg,font=fnt).grid(row=0,column=0)
Label(frame,text='Name:',bg=bg,fg=fg,font=fnt).grid(row=1,column=0)
Label(frame,text='Address:',bg=bg,fg=fg,font=fnt).grid(row=2,column=0)
strid = StringVar()
strname = StringVar()
straddress = StringVar()

txtid = Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=strid)
txtname = Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=strname)
txtaddress = Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=straddress)

txtid.grid(row=0,column=1,pady=pad)
txtname.grid(row=1,column=1,pady=pad)
txtaddress.grid(row=2,column=1,pady=pad)

def createemployeefile():
    if strid.get().strip()=='':
        messagebox.showinfo('info','The ID is empty Please try again !')
        txtid.focus()
    elif strname.get().strip()=='':
        messagebox.showinfo('name empty','The name is empty Please try again !')
        txtname.focus()
    elif straddress.get().strip()=='':
        messagebox.showinfo('address empty','The Address is empty Please try again !')
        txtaddress.focus()
    else:
        filename = strid.get()+'_'+ strname.get() +'.csv'
        f = open(filename,'w+')
        f.write('ID: '+ strid.get()+ '\n')
        f.write('Name: '+ strname.get()+ '\n')
        f.write('Address: '+ straddress.get()+ '\n')
        f.close()
        messagebox.showinfo('secsse','Employee file is Created :)')
        strid.set('')
        strname.set('')
        straddress.set('')
        txtid.focus()

btnstyle = ttk.Style()
btnstyle.configure('TButton',bg=bg,font=fnt,pady=pad,padding=pad)
ttk.Button(frm,text='Create employee file now',style='TButton',command=createemployeefile).pack(pady=pad)
ttk.Button(frm,text='Exit',style='TButton',command=frm.destroy).pack(pady=pad)

frm.mainloop()