from tkinter import *

window = Tk()

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    # Corrige o cálculo da posição final
    x = widget.winfo_x() + (event.x - widget.startX)
    y = widget.winfo_y() + (event.y - widget.startY)
    widget.place(x=x, y=y)

# Cria o primeiro label
label = Label(window, bg='red', width=10, height=5)
label.place(x=0, y=0)
label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)  # Evento correto para mover enquanto arrasta

# Cria o segundo label
label2 = Label(window, bg='blue', width=10, height=5)
label2.place(x=100, y=100)
label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)  # Evento correto para mover enquanto arrasta

window.mainloop()
