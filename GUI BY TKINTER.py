from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("BRO NANANINARE NANINENARO")
window.config(background = "black")
window.mainloop()  # place window on screen

# for i#age and text in the window

from tkinter import *

window = Tk()
window.geometry("650x650")
window.title("BRO NANANINARE NANINENARO")
window.config(background = "black")


photo = PhotoImage(file = 'picture.png')
label = Label(window,text = "sabaash hackerrrr!!",  #for adding text
              font=('Arial',20,'bold'),   #for font,size and type
              fg ="red",                  #for font colour
              bg = 'black',               #for font background
              relief = RAISED,            #for border type
              bd = 30,                    #for border length
              padx = 20,                  #for distance from x-axis of border
              pady = 20,                  #for distance from y-axis of border
              image = photo,              #for photo
              compound = 'top'         #so that it know where to put photo regards to text
              )
# label.place(x=0,y=1)
label.pack()

window.mainloop()  # place window on screen



