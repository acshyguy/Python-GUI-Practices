# from tkinter import *
# def say_hi():
#  print("hello ~ !")

# root = Tk()

# frame1 = Frame(root)
# frame2 =Frame(root)
# root.title("tkinter frame")

# Label= Label(frame1, text="Label", justify=LEFT, width=80)
# Label.pack(side=LEFT)

# hi_there = Button(frame2, text="say hi~", command=say_hi)
# hi_there.pack()

# frame1.pack(padx = 1, pady= 1)
# frame2.pack(padx = 10, pady= 10)

# root.mainloop()


## Adding photo 
from tkinter import *

root = Tk()

textLabel = Label(root, text="My Cat 'Oreo'", justify=LEFT, padx=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="forest_image.png")
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)

mainloop()

