from tkinter import *

frm = Tk()
frm.geometry('800x600')

lblbox = Listbox(frm,foreground='pink',background='darkred')
lblbox.insert(0,'Gera')
lblbox.insert(1,'jena')
lblbox.insert(2,'Erfurt')
lblbox.insert(3,'Altenburg')
lblbox.insert(4,'schmölln')
lblbox.pack()
def printf():
    print(lblbox.get(ACTIVE))
Button(frm,text='ok',command=printf).pack()
frm.mainloop()