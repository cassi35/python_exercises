from tkinter import * 
from time import *
window = Tk()
def update():
    time_string = strftime("%I:%M:%S")
    time_label.config(text=time_string)
    time_label.after(1000,update)
time_label = Label(window,font=('Arial',50),fg='#00FF00',bg='black')
time_label.pack()
update()
window.mainloop()