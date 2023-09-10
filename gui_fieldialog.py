# import tkinter as tk
# from tkinter import filedialog as fd

# def callback():
#     name = fd.askopenfilename()
#     print(name)

# errmsg = 'Error!'
# tk.Button(text='Click to Open File', command=callback).pack(fill=tk.X)
# tk.mainloop()


### We use the previous image upload file and opened it
from tkinter import *
from PIL import Image, ImageTk

from tkinter import filedialog as fd
import tkinter as tk

def callback():
     name = fd.askopenfilename()
     print(name)
     return name
class Window(Frame):
    def __init__(self, master = None):
        Frame. __init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open(callback())
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
    
    

root = Tk()
app = Window(root)
root.wm_title("Tkinter Window showing Chicken")

#tk.Button(text='Click to Open File', command=callback).pack(fill=tk.X)

root.geometry("200x120")
root.mainloop()
