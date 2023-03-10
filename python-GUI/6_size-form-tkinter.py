# Learn Python in Arabic #127 -واجهات بايثون Python gui حجم الفورم size form tkinter Python in Arabic
import tkinter
frm = tkinter.Tk()
frm.geometry('600x400')
frm.update()
w = frm.winfo_width()
h = frm.winfo_height()
frm.title(str(w)+'x'+ str(h))

frm.mainloop()