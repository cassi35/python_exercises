from tkinter import *
window = Tk()
window.geometry('400x400')
window.title('scale')
coldimage = PhotoImage(file='/home/cassiano/backuptodos/pendrive/python_exercises/tkinker/cold.png')
hotimage = PhotoImage(file='/home/cassiano/backuptodos/pendrive/python_exercises/tkinker/temperatura-alta.png')

scale = Scale(window,from_=0,to=100,width=20,
              length=300,orient=VERTICAL,tickinterval=10,
              resolution=5,troughcolor='#2f6e65',fg='#1a5422',bg='#a8ede5')
scale.pack()
def submit():
    if scale.get() > 50:
        label = Label(window,image=hotimage)
        label.pack()
    else:
        label = Label(window,image=coldimage)
        label.pack()
        
button = Button(window,text='submit',command=submit)
button.pack()
window.mainloop()