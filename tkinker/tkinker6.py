from tkinter import *
window = Tk()
window.geometry('400x400')
window.title('foods')
food = ['pizza','hamburger','hotdog']
x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,text=food[index],
                              variable=x,
                            #   bg='#1a3834',
                            #   ,bd=1,fg='white'
                            #   ,pady=10,
                            #   padx=10,
                              value=index,
                              padx=25,
                              font=('Impact',20))
    radiobutton.config()
    radiobutton.pack(anchor=W)#para deixar na esquerda
window.mainloop()