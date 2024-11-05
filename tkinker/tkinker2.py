# lables 
from tkinter import *
window = Tk()
window.geometry('420x120')
window.title('labels')
photo = PhotoImage(file='/home/cassiano/backuptodos/pendrive/python_exercises/tkinker/icons8-selecionado-80.png')
label = Label(window,text="hello world",font=('Arial',40,'bold'),fg='green',
              image=photo,
              bd=10,
              padx=20,
              pady=20,
              compound='left')#aonde a imagem fica 
# label.place(x=100,y=50) em pixels
label.pack() #deixa no centro 

window.mainloop()