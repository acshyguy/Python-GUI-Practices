import tkinter

# Init tk
root = tkinter.Tk()

#create canvas
myCanvas = tkinter.Canvas(root, bg="black", height=300, width=300)

# draw arcs
coord = 10, 10, 300, 300
#arc = myCanvas.create_arc(coord, start=0, extent=150, fil="red")
#arc2 = myCanvas.create_arc(coord, start=150, extent=215, fil="green")

## Creating a line
# strokes = 0,0, 60,180, 260,50, 0,280
# line = myCanvas.create_line(strokes, fill= "black")

## Creating a polygon
strokes = 100,100, 200,200, 150,10, 100,100
line = myCanvas.create_polygon(strokes, fill= "red")

#add to window and show
myCanvas.pack()
root.mainloop()
