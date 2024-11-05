# widgets ==> gui elements buttons,textboxes, labels, images
# windows ==> server as container 
# to hold or contain these widgets
from tkinter import *
window = Tk()
window.geometry('420x120')
window.title('first code cassiano')
icon = PhotoImage(file='/home/cassiano/backuptodos/pendrive/python_exercises/tkinker/icons8-selecionado-80.png')
window.iconphoto(True,icon)
window.config(background="#1e695a")
window.mainloop()