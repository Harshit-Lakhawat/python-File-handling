# creating scale in python

from tkinter import *
from PIL import Image, ImageTk

def submit():
    print("The temperature is : "+ str(scale.get())+ " degrees C")

window = Tk()

scale = Scale(window,from_=100,to=0,
              bg = "grey",
              fg = "black",
              troughcolor = "red",
              font = ('Consolas',20),
              length = 400,
              orient = VERTICAL,
              tickinterval = 10,
              showvalue = 0,   #hide the current value from scale
              )

#scale.set(50) #set the value at start use for#ula for better
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window,text = 'Submit',command=submit)
button.pack()
window.mainloop()




# creating listbox in python

from tkinter import *
from PIL import Image, ImageTk

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You Have Ordered : ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg = "brown",
                  font = ("Constantia",35),
                  width = 12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height = listbox.size())

entrybox = Entry(window)
entrybox.pack()

submitbutton = Button(window, text= "Submit",command = submit)
submitbutton.pack()

addbutton = Button(window, text= "Add",command = add)
addbutton.pack()

deletebutton = Button(window, text= "Delete",command = delete)
deletebutton.pack()

window.mainloop()
