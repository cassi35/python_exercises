from tkinter import *
window = Tk()
menubar = Menu(window)
window.config(menu=menubar)
filemenu = Menu(menubar,tearoff=0)
def openfile():
    print('file has been oppened')
def savefile():
    print('file has been saved')
menubar.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='open',command=openfile)
filemenu.add_command(label='save',command=savefile)
filemenu.add_separator()
filemenu.add_command(label='exit',command=quit)  
edit_menu = Menu(menubar,tearoff=0)
def cut():
    print('file has been cuted')
def copy():
    print('file has been copied')
def paste():
    print('file has been pasted')
menubar.add_cascade(label='edit',menu=edit_menu )
edit_menu.add_command(label='cut',command=cut)
edit_menu.add_command(label='copy',command=copy)
edit_menu.add_command(label='paste',command=paste)
window.mainloop()