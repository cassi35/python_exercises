from tkinter import *
from tkinter.ttk import *
import time
window = Tk()
window.geometry('420x420')
window.title('time')
def start():   
    GB = 10
    download = 0 
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(((download/GB)*100))+"%")
        text.set(str(download)+'/'+str(GB)+"task is completed")
        window.update_idletasks()

bar = Progressbar(window,orient=HORIZONTAL)
bar.pack(padx=10,pady=10)
percent = StringVar()
text = StringVar()
percentLabel = Label(window,textvariable=percent)
percentLabel.pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text='clique no botao',command=start)
button.pack(padx=10)
window.mainloop()
