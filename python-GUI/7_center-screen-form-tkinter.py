# Learn Python in Arabic #128 - gui الفورم في المنتصف center screen form tkinter Python in Arabic
import tkinter 
frm= tkinter.Tk()
w = 500
h = 300
sw = frm.winfo_screenwidth()
sh = frm.winfo_screenheight()
x = ( sw-w )/ 2
y = ( sh-h ) /2

frm.geometry('%dx%d+%d+%d' % (w,h,x,y))


frm.mainloop()