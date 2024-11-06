from tkinter import *
# from tkinker import grid
window = Tk()
firstlabel = Label(window,text='first anme').grid(row=0,column=0)
fisrtNameEtry = Entry(window).grid(row=0,column=1)

lastLabel = Label(window,text='last anme').grid(row=1,column=0)
lastNameEtry = Entry(window).grid(row=1,column=1)

emailLabel = Label(window,text='email: ').grid(row=2,column=0)
emailEtry = Entry(window).grid(row=2,column=1)
window.mainloop()
