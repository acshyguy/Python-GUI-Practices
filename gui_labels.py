import time
from tkinter import *
class App(Frame):
    def __init__(self, master = None):
        Frame. __init__(self, master)
        self.master = master
        self.label = Label(text="", fg="Red", font=("Helvetica", 26))
        self.label.place(x=50, y=80)
        self.update_clock()
        

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

## initialize tkinter
root = Tk()
app = App(root)
root.wm_title("Tkinter clock")

root.geometry("320x200")
root.after(1000, app.update_clock)
root.mainloop()

