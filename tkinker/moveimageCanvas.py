from tkinter import *

window = Tk()

def move_up(event):
    canvas.move(myimage, 0, -10)

def move_down(event):
    canvas.move(myimage, 0, 10)

def move_left(event):
    canvas.move(myimage, -10, 0)

def move_right(event):
    canvas.move(myimage, 10, 0)

# Vincula as teclas de direção
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

# Configura o Canvas e imagem
canvas = Canvas(window, width=500, height=500)
canvas.pack()
photoimage = PhotoImage(file='/home/cassiano/Área de trabalho/cassianoUbuntu/coisasUbuntuBackUp/python_exercises/python_exercises/tkinker/icons8-selecionado-20.png')
myimage = canvas.create_image(0, 0, anchor=NW, image=photoimage)

window.mainloop()