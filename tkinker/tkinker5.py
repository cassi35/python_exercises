from tkinter import *
window = Tk()
window.geometry('400x400')
x = IntVar()
def display():
    if (x.get()== 1):
        print('you agree')
    else:
        print('you dont agree')
photo = PhotoImage(file='/home/cassiano/backuptodos/pendrive/python_exercises/tkinker/icons8-selecionado-20.png')
check_button = Checkbutton(window,text='I agree something'
                           ,variable=x
                           ,onvalue=1
                           ,offvalue=0
                           ,command=display
                           ,font=('Arial',20)
                           ,fg='#1a3840'
                           ,padx=25
                           ,pady=25
                           ,image=photo
                           ,compound='right')
check_button.pack()
window.mainloop()