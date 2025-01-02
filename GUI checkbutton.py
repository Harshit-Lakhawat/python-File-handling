# creating chackbutton in python

from tkinter import *
from PIL import Image, ImageTk

window = Tk()

def display():
    if(x.get() == 1):
        print("haa sahabjii")
    else:
        print("naa sahabjii")

x = IntVar()
# Load and resize the image
original_image = Image.open('like.png')
desired_width = 100 # set the width
desired_height = 60  # set the height
resized_image = original_image.resize((desired_width,desired_height),Image.Resampling.LANCZOS)  #use so that quality of i#age is good Image.Resampling.LANCZOS
photo = ImageTk.PhotoImage(resized_image)


check_button = Checkbutton(window,
                           text = "hello bhaisahab",
                           variable = x,
                           onvalue = 1,
                           offvalue = 0,
                           command = display,
                           font = ('Arial',20),
                           fg = "red",
                           bg = "black",
                           activeforeground = "red",
                           activebackground = "black",
                           padx = 25,
                           pady = 10,
                           image = photo,
                           compound = "left")

check_button.pack()

window.mainloop()
