from tkinter import ttk
def tkcnter(frm):
    frm.update()
    fw = frm.winfo_width()
    fh = frm.winfo_height()
    sw = frm.winfo_screenwidth()
    sh = frm.winfo_screenheight()
    x = ( sw-fw ) / 2
    y = ( sh-fh ) / 2 -45
    frm.geometry('%dx%d+%d+%d' % (fw,fh,x,y))

def backgroundall(frm,bg):
    frm.update()
    ctrls = frm.winfo_children()
    frm.config(bg=bg)
    for c in ctrls:
        classinfo =  c.winfo_class()
        if classinfo=='Label'or classinfo == 'Button' or classinfo =='Entry':
            c['bg']=bg
        if classinfo=='TLabel'or classinfo == 'TButton' or classinfo =='TEntry':
            mystyle = ttk.Style()
            mystyle.configure('TLabel',background = bg)
            mystyle.configure('TButton',background = bg)
            mystyle.configure('TEntry',background = bg)
            