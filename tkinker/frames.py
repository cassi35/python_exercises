from tkinter import *
window = Tk()
frame = Frame(window,bg='pink',bd=5,relief=RAISED)
frame.pack()
button = Button(frame,text='W',font=(('Consolas',35)),width=3).pack(side=TOP)
button = Button(frame,text='A',font=(('Consolas',35)),width=3).pack(side=LEFT)
button = Button(frame,text='S',font=(('Consolas',35)),width=3).pack(side=LEFT)
button = Button(frame,text='D',font=(('Consolas',35)),width=3).pack(side=LEFT)

window.mainloop()