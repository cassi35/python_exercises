from tkinter import *
def create_window():
        # new_window = Toplevel()
        # new_window.mainloop()
        new_window = Tk()
        old_window.destroy() 
old_window = Tk()
old_window.geometry('420x420')
button = Button(old_window,text='enviar',command=create_window).pack()
old_window.mainloop()