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
