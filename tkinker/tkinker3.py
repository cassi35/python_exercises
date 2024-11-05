from tkinter import *
window = Tk()
window.geometry('420x120')
window.title('labels')
image = PhotoImage(file='/home/cassiano/backuptodos/pendrive/python_exercises/tkinker/icons8-selecionado-20.png')
def click():
    label = Label(window,text='very good you clicked the button',image=image,compound='right')
    label.pack()
button = Button(
                window,text='click me',command=click,font=('Comic Sans',30),
                fg='white',
                bg='black',
                activeforeground='black',
                activebackground='#0d6775',
                state=ACTIVE,
                )
button.pack()
window.mainloop()