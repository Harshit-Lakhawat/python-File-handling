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




# mouse event

from tkinter import *

def dosomething(event):
    #print("you did a thing")
    print("mouse coordinates : " + str(event.x)+ "," +str(event.y))

window = Tk()

#window.bind("<Button-1>",dosomething)           #on left click it works
#window.bind("<Button-2>",dosomething)           #on middle wheel of mouse if we click it works
#window.bind("<Button-3>",dosomething)           #on right click it works
#window.bind("<ButtonRelease>",dosomething)      #one we press the mouse then where we release it
#window.bind("<Enter>",dosomething)              #from where our mouse enter in window
#window.bind("<Leave>",dosomething)              #from where our mouse leave in window
window.bind("<Motion>",dosomething)              #as long as Mouse is in Motion

window.mainloop()
