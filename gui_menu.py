from tkinter import *
class Window(Frame):
    def __init__(self, master = None):
        Frame. __init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu = menu)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)
        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        self.pack(fill=BOTH, expand=1)
        text = Label(self, text="Just do it")
        text.place(x=70, y=90)


    def exitProgram(self):
        exit()

root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x200")
root.mainloop()


