# Learn Python in Arabic #152 - واجهات بايثون Python gui عرض صورة show image tkinter Python in Arabic
from tkinter import *

frm = Tk()
frm.geometry('900x600')

canvas = Canvas(frm,width=500,height=400)
canvas.pack()
img = PhotoImage(file='your path to image')
canvas.create_image(0,0, Image= img)

frm.mainloop()