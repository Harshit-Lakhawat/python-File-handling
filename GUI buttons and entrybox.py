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





# creating entrybox in python

from tkinter import *
from PIL import Image, ImageTk

def submit():
    username = entry.get()
    print(f" hello {username} ")
    entry.config(state = DISABLED)   #this will disable the entrybox after sub#it

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)


# Initialize the main window
window = Tk()
window.title("sexy hora BKL")
window.config(background = "black")

entry = Entry(window,
              font=('Arial',50),
              fg = "red",
              bg ="black",
              show = '*'    #used so that in entrybox only * this is shown
              )
#entry.insert(0,'PASSWORD ')  #insert at start of entrybox
entry.pack(side = LEFT)

submit_button = Button(window,
                       text = "SUBMIT",
                       command = submit
                       )
submit_button.pack(side = RIGHT)

delete_button = Button(window,
                       text = "DELETE",
                       command = delete
                       )
delete_button.pack(side = RIGHT)

backspace_button = Button(window,
                       text = "BACKSPACE",
                       command = backspace
                       )
backspace_button.pack(side = RIGHT)

window.mainloop()
