# import wikipedia
# from gtts import gTTS
# import os

# ## QUESTION 1
# ## Integrate wikipedia with gTTS by prompting a user to enter a search
# search = input("Enter what u want to search here: ")
# result = wikipedia.summary(search, sentences = 3)
# language = "en"
# myobj = gTTS(result, lang= language,slow=False)

# myobj.save("voice.mp3")

# os.system("mediaplayer voice.mp3")

# print(myobj)



### QUESTION 2

# ## For Plain Window
from tkinter import *
import tkinter as tk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
    #For Labels
Window = tk.Tk()
Window.geometry('500x300')
e1 = tk.Entry(Window, show=None, font=("Arial", 14))
e2 = tk.Entry(Window, show=None, font=("Arial", 14))
e3 = tk.Entry(Window, show="*", font=("Arial", 14))


# initialize tkinter
root = Tk()
app = Window(root)
# set window title
root.wm_title("Tkinter window")

# For Labels
e1.pack()
e2.pack()
e3.pack()

# show window
root.mainloop()




# #For Lable
# import tkinter as tk

# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')

# e1 = tk.Entry(window, show=None, font=("Arial", 14))
# e2 = tk.Entry(window, show=None, font=("Arial", 14))
# e3 = tk.Entry(window, show="*", font=("Arial", 14))
# e1.pack()
# e2.pack()
# e3.pack()

# window.mainloop()



# ## For Buttons
# from tkinter import *
# class Window(Frame):
#     def __init__(self, master = None):
#         Frame. __init__(self, master)
#         self.master = master

#         #widget can take all window
#         self.pack(fill = BOTH, expand = 1)
#         #create button, link it to clickExitButton()
#         exitButton = Button(self, text="Exit", command=self.clickExitButton)
#         #place button at (0,0)
#         exitButton.place(x=0, y=0)

#     def clickExitButton(self):
#         exit()

# ## initialize tkinter
# root = Tk()
# app = Window(root)
# ##set window
# root.wm_title("Tkinter window")

# root.geometry("320x200")
# ## show window
# root.mainloop()