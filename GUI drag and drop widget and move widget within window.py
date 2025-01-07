# drag and drop widget

from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startx= event.x
    widget.starty= event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startx + event.x
    y = widget.winfo_y() - widget.starty + event.y
    widget.place(x=x,y=y)

window = Tk()

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()





# move widget within window

from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("500x500")

racecar_image = Image.open('racecar.png')
desired_width = 250# set the width
desired_height = 150  # set the height
resized_image = racecar_image.resize((desired_width,desired_height),Image.Resampling.LANCZOS)  #use so that quality of i#age is good Image.Resampling.LANCZOS
racecarimage = ImageTk.PhotoImage(resized_image)

label = Label(window,image=racecarimage)
label.place(x=0,y=0)

window.mainloop()


