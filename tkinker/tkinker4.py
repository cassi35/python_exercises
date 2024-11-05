from tkinter import *
window = Tk()
entry = Entry(window,font=('Arial',50),fg='green',bg='black',show='*')
entry.pack(side=LEFT)
entry.insert(0,'name: ')
def submit():
    username = entry.get() 
    print('hello:'+username)
    entry.config(state=DISABLED)
submit_button = Button(window,text='submit',command=submit)
submit_button.pack(side=RIGHT)
def delete():
    entry.delete(5,END)
delete_button = Button(window,text='delete',command=delete)
delete_button.pack(side=LEFT)

def backspace():
    entry.delete(len(entry.get())-1,END)

backspace_button = Button(window,text='backspace',command=backspace)
backspace_button.pack(side=LEFT)
window.mainloop()