# new window

from tkinter import *
from tkinter import filedialog


def create_window():
    #new_window = Toplevel()   #a newwindow occur linked
# with old window if we close old new auto#atically gets closed
    new_window = Tk()          # new independent window
    old_window.destroy()       #to destroy old when new created


old_window = Tk()

Button(old_window,text = "create new window",command=create_window ).pack()

old_window.mainloop()
