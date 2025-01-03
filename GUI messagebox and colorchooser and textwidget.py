# creating messagebox in python

from tkinter import *
from tkinter import messagebox

window = Tk()

def click():
    #messagebox.showinfo(title = "info bro ", message = "hello bhai kya haal")
    #messagebox.showwarning(title="WARNING ", message="BHAAGOO BEHENCHOOO ")
    #messagebox.showerror(title="ERROR ", message="CHUD GAYE ")

    #if messagebox.askokcancel(title="ask ok cancel ", message="karna chahta h? "):
        #print("YOU DID A THING ")
    #else:
        #print("YOU DID NOTHING")

     #if messagebox.askretrycancel(title="ask retry cancel ", message="karna chahta h vapis? "):
         #print("YOU RETRIED A THING ")
    #else:
         #print("YOU DIDNOT RETRIED ")

    #if messagebox.askyesno(title="ask yes or no ", message="kya tujhe pasand h? "):
        #print("mujhe bhi pasand h")
    #else:
        #print("pasand hona chahiye")

    answer =  messagebox.askyesnocancel(title="ask yes no cancel ", message="do you like coding?",icon ='error')
    if(answer == True):
        print("YOU ARE LIKE mE YOU ALSO LIKE CODING")
    elif (answer == False):
        print("YOU SHOULD STOP CODING AS YOU DONOT LIKE IT")
    else:
        print("YOU DODGED THE QUESTION")


button = Button(window,command = click, text = "click me")
button.pack()

window.mainloop()




# creating colorchooser in python

from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)      #this show RBG values then hexadecimal value
    colorhex = color[1]
    print(colorhex)
    window.config(bg = colorhex)

window = Tk()
window.geometry("420x420")
button = Button(text = "click for colors", command = click)
button.pack()

window.mainloop()




# creating textwidget in python

from tkinter import *


def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text = Text(window,bg ="light yellow",
            font = ("Ink Free",25),
            height = 8,
            width = 20,
            padx = 20,
            pady =20,
            fg = "red")
text.pack()

button = Button(window,text = "Submit", command = submit)
button.pack()

window.mainloop()



