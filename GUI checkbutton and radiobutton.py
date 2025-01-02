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







# creating radiobutton in python

from tkinter import *
from PIL import Image, ImageTk

food = ["pizza", "hotdog", "burger"]

window = Tk()

def order():
    if(x.get() == 0):
        print("YOU ORDERED PIZZA")
    elif(x.get() == 1):
        print("YOU ORDERED HOTDOG")
    elif(x.get() == 2):
        print("YOU ORDERED BURGER")
    else:
        print("WTF")


window.title("ye kya huiii")
window.config(background = "black")

# Load and resize the pizza image
pizza_image = Image.open('pizza.png')
desired_width = 200  # set the width
desired_height = 100  # set the height
resized_image = pizza_image.resize((desired_width,desired_height),Image.Resampling.LANCZOS)  #use so that quality of i#age is good Image.Resampling.LANCZOS
pizzaimage = ImageTk.PhotoImage(resized_image)

# Load and resize the hotdog image
hotdog_image = Image.open('hotdog.png')
desired_width = 200  # set the width
desired_height = 100  # set the height
resized_image = hotdog_image.resize((desired_width,desired_height),Image.Resampling.LANCZOS)  #use so that quality of i#age is good Image.Resampling.LANCZOS
hotdogimage = ImageTk.PhotoImage(resized_image)

# Load and resize the burger image
burger_image = Image.open('burger.png')
desired_width = 200  # set the width
desired_height = 100  # set the height
resized_image = burger_image.resize((desired_width,desired_height),Image.Resampling.LANCZOS)  #use so that quality of i#age is good Image.Resampling.LANCZOS
burgerimage = ImageTk.PhotoImage(resized_image)

foodimage = [pizzaimage,hotdogimage,burgerimage]


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window, text = food[index],
                              variable = x,  #group radiobutton together
                              value = index,  #assign each radiobutton a diff value
                              padx = 25,
                              font=('Impact',50),
                              bg="black",
                              fg = "red",
                              activeforeground = "red",
                              activebackground = "black",
                              image = foodimage[index],
                              compound="left",
                              indicatoron=0, #eli#inate circles fr# start
                              width = 500,  #to set the button width
                              command = order)
    radiobutton.pack(anchor=W)   #anchor=W so that it allign in same line

window.mainloop()
