from tkinter import *
from tkinter import colorchooser    
window = Tk()
window.geometry('420x420')
def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)
button = Button(text='click',command=click)
button.pack()
window.mainloop()