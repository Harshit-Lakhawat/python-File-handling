#menubar

from tkinter import *
from tkinter import filedialog

def openfile():
    print("file has been opened! ")

def savefile():
    print("file has been saved! ")

def cut():
    print("file has been cut! ")

def copy():
    print("file has been copied! ")

def paste():
    print("file has been pasted! ")

window = Tk()

menubar = Menu(window)
window.config(menu = menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="open",command=openfile)
filemenu.add_command(label="save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="exit",command=quit)

editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="edit",menu=editmenu)
editmenu.add_command(label="copy",command=copy)
editmenu.add_command(label="paste",command=paste)
editmenu.add_separator()
editmenu.add_command(label="cut",command=cut)


window.mainloop()





# frame

from tkinter import *
from tkinter import filedialog

window = Tk()

frame = Frame(window, bg = "light yellow",bd=5,relief=SUNKEN)
#frame.pack(side = BOTTOM)     #place frame at bottom
frame.place(x=0,y=0)           #place frame at cooredinates

button = Button(frame,text="W",font=("Consolas",25),width = 3)
button.pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width = 3).pack(side =LEFT)
Button(frame,text="S",font=("Consolas",25),width = 3).pack(side =LEFT)
Button(frame,text="D",font=("Consolas",25),width = 3).pack(side =LEFT)

window.mainloop()


