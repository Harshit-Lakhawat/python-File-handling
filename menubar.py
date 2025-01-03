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
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0 ) #to get rid of line on top tearoff=0
menubar.add_cascade(label="file", menu =filemenu)
filemenu.add_command(label="open",command=openfile)
filemenu.add_command(label="save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="exit",command=quit)


editmenu = Menu(menubar, tearoff=0 )
menubar.add_cascade(label="edit", menu=editmenu)
editmenu.add_command(label="cut",command=cut)
editmenu.add_command(label="save",command=copy)
editmenu.add_separator()
editmenu.add_command(label="paste",command=paste)

window.mainloop()
