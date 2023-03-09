import tkinter as tk
frm = tk.Tk()
getinfo = str(frm.winfo_screenwidth())+'x' +str (frm.winfo_screenheight())  
frm.title(getinfo)
frm.geometry('500x250+700+250')



frm.mainloop()