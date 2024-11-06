from tkinter import *
window = Tk()
window.geometry('420x420')
window.title('text area')
def submit():
    input = text.get('1.0',END)
    print(input)
text = Text(window,height=8,width=20
            ,padx=20,pady=20)
text.pack()
button = Button(window,text='submit',command=submit)
button.pack()
window.mainloop()