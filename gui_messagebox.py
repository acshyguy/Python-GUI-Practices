import tkinter
import tkinter.messagebox

def buttonClick():
    ### Run these methods below seperately

    # tkinter.messagebox.showinfo('title', 'message')  ##Method 1
    #tkinter.messagebox.showwarning('title', 'Review coz u're warned!')##Method 2
    tkinter.messagebox.showerror('title', 'U hv error')##Method 3


root = tkinter.Tk()
root.title('GUI')
root.geometry('100x100')
root.resizable(False, False)
tkinter.Button(root, text='hello button', command=buttonClick).pack()
root.mainloop()