from tkinter import *
window = Tk()
import time
WIDTH = 500
HEIGHT = 500
xvelocity = 1
yvelolyty = 1
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
photo_image = PhotoImage(file='/home/cassiano/Área de trabalho/cassianoUbuntu/coisasUbuntuBackUp/python_exercises/python_exercises/tkinker/icons8-selecionado-20.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)
image_width = photo_image.width()
image_right = photo_image.height()
while True:
    cordinates = canvas.coords(my_image)
    print(cordinates)
    if(cordinates[0]>= WIDTH or cordinates[0] < 0):
        xvelocity = -xvelocity
    canvas.move(my_image,xvelocity,0)
    window.update()
    time.sleep(0.01)

window.mainloop()   