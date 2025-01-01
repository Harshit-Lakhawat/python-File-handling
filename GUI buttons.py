# creating button in python

from tkinter import *
from PIL import Image, ImageTk

count = 0
# Initialize the main window
window = Tk()
window.geometry("300x300")
window.title("ye kya huiii")
window.config(background = "black")

# Load and resize the image
original_image = Image.open('like.png')
desired_width = 200  # set the width
desired_height = 100  # set the height
resized_image = original_image.resize((desired_width,desired_height),Image.Resampling.LANCZOS)  #use so that quality of i#age is good Image.Resampling.LANCZOS
photo = ImageTk.PhotoImage(resized_image)

def click():
    global count
    count+=1
    print(count)

button = Button(window, text = "click me",
                command = click,
                font = ("Comic Sans",30),
                fg = "red",
                bg = "black",
                activeforeground = "red",    #so that it didnot flash text
                activebackground = "black",  #so that it didnot flash background
                # state =DISABLED              #to disable clicking its always able if we dont give disable
                image = photo,
                compound = 'bottom'
                )
button.pack()

window.mainloop()
