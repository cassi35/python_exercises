from tkinter import *
from tkinter import messagebox
def click():
    # messagebox.showinfo('this is info message box',message='are you sure? ')
    # messagebox.showwarning('this is info message box',message='are you sure? ')
    # messagebox.showerror('this is info message box',message='something went wrong ')
    # if messagebox.askokcancel(title='ask to cancel',message='do you want do the thing??'):
    #     print('you did the thing')
    # else:
    #     print('you did not thing')
    # mensagebol = messagebox.askyesno(title='ask yes or no',message='do you like cake?')
    # if mensagebol:
    #     print('you like cake')
    # else:
    #     print('you dont like cake')
    # asnwer = messagebox.askquestion(title='ask question',message='do you like pie?')
    # if asnwer =='sim':
    #     print('ok')
    # else:
    #     print('not ok')
    
    pass
window = Tk()
window.geometry('400x400')
button = Button(window,command=click,text='click me !')
button.pack()
window.mainloop()