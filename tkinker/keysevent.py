from tkinter import *

# Função para capturar teclas pressionadas
def dosomething(event):
    # print("Você pressionou a tecla:", event.keysym)
    label.config(text=event.keysym)

# Janela principal
window = Tk()
window.geometry('420x420')
label = Label(window,font=("Helvetica",100))
label.pack()
window.bind("<Key>", dosomething)  # Vincula qualquer tecla pressionada à função `dosomething`
window.mainloop()
