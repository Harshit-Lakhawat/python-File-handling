from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("BRO NANANINARE NANINENARO")
window.config(background = "black")
window.mainloop()  # place window on screen



# for i#age and text in the window

from tkinter import *
from PIL import Image, ImageTk


window = Tk()
window.geometry("650x650")
window.title("BRO NANANINARE NANINENARO")
window.config(background = "black")

# Load and resize the image
original_image = Image.open('picture.png')
desired_width = 200  # set the width
desired_height = 100  # set the height
resized_image = original_image.resize((desired_width,desired_height),Image.Resampling.LANCZOS)  #use so that quality of i#age is good Image.Resampling.LANCZOS
photo = ImageTk.PhotoImage(resized_image)

label = Label(window,text = "sabaash hackerrrr!!",  #for adding text
              font=('Arial',20,'bold'),   #for font,size and type
              fg ="red",                  #for font colour
              bg = 'black',               #for font background
              relief = RAISED,            #for border type
              bd = 30,                    #for border length
              padx = 20,                  #for distance from x-axis of border
              pady = 20,                  #for distance from y-axis of border
              image = photo,              #for photo
              compound = 'bottom'         #so that it know where to put photo regards to text
              )
# label.place(x=0,y=1)
label.pack()

window.mainloop()  # place window on screen
