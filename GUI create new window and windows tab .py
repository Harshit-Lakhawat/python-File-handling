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




# windows tab

from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)  #widget that manages a collectio of windows/display

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text="Tab1")
notebook.add(tab2,text="Tab2")
notebook.pack(expand=True,fill="both")   #expand to fill any space not otherwise used
                                        #fill space on x and y axis

Label(tab1,text = "this is tab 1", width=50, height=25).pack()
Label(tab2,text = "this is tab 2", width=50, height=25).pack()

window.mainloop()
