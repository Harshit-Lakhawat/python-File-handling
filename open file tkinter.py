#opwn a file by filedialog

from tkinter import *
from tkinter import filedialog

window = Tk()

def openfile():
    filepath = filedialog.askopenfilename()
    file = open(filepath,'r')
    print(file.read())
    file.close()

button = Button(text="open",command = openfile)
button.pack()

window.mainloop()
