from tkinter import *
window = Tk()
window.geometry('400x400')
listbox = Listbox(window)
listbox.pack()
listas = ['programacao','estudo','carro']
for i in range(len(listas)):
    listbox.insert(i,listas[i])
listbox.config(height=listbox.size())
def submit():
    print( listbox.get(listbox.curselection()) )
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
entrybox = Entry(window)
entrybox.pack()
submit_button = Button(window,text="submit",command=submit)
submit_button.pack()

add_button = Button(window,text="add",command=add)
add_button.pack()

delete_button = Button(window,text="delete",command=delete)
delete_button.pack()
window.mainloop()