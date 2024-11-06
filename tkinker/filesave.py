from tkinter import *
from tkinter import filedialog
window = Tk()
def savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt',initialdir='/home/cassiano/backuptodos/pendrive/python_exercises/exercisesDataStructure',
                                    filetypes=[("text file",".txt")
                                                                       ,("html file",".html")])
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()
button = Button(text='save',command=savefile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()