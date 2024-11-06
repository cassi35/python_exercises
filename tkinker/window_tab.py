from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry('420x420')
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1,text='tab 1')
notebook.add(tab2,text='tab 2')
notebook.pack(expand=True,fill='both')
Label(tab1,text='this is text numeber one',width=50,height=25).pack()
Label(tab2,text='this is text numeber two',width=50,height=25).pack()
window.mainloop()