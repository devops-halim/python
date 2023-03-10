# Learn Python in Arabic #129 - gui الفورم منع تغيير الحجم resizable form tkinter Python in Arabic
import tkinter
frm = tkinter.Tk()
frm.geometry('600x400')
frm.resizable(False,False)
frm.mainloop()