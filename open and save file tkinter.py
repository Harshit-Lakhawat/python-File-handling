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




#save a file by filedialog

from tkinter import *
from tkinter import filedialog

window = Tk()

def savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text file",".txt"),
                                               ("Html file",".html"),
                                               ("All files",".*")])
    #filetext = str(text.get('1.0', END))     #by this we can write text in window
    filetext = input("Enter some text : ")  #by this we can write text in consol
    file.write(filetext)
    file.close()

button = Button(text="save",command = savefile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()
