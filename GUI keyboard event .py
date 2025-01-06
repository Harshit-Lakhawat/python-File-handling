# keyboard event which key i am pressing in tkinter

from tkinter import *

def dosomething(event):
    #print("you pressed : "+ event.keysym)
     label.config(text=event.keysym)    #by this it will print key which we press on window in label
window = Tk()

window.bind("<Key>",dosomething)

label = Label(window,font=("Helvetica",40))
label.pack()

window.mainloop()
