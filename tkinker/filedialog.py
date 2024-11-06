from tkinter import *
from tkinter import filedialog
window = Tk()
window.geometry('420x420')
def openfile():
    filepath = filedialog.askopenfilename(title='open the file inglesh',
                                          filetypes=(('text files',"*.txt"),('all files','*.*')))
    file = open(filepath,'r')
    print(file.read())
    file.close()
button = Button(text='open',command=openfile)
button.pack()
window.mainloop()