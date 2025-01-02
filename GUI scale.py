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

