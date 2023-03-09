# Learn Python in Arabic #125 - gui ابعاد الشاشة screen width height form tkinter Python in Arabic
import tkinter
frm = tkinter.Tk()
psinfo = str (frm.winfo_screenwidth()) + 'x' + str (frm.winfo_screenheight())
frm.title(psinfo)
frm.geometry('700x600')
frm.mainloop()