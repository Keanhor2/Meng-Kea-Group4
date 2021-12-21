import tkinter as tk
import random
root=tk.Tk()
root.geometry("800x800")
frame=tk.Frame()
frame.master.title("Friends Help")
canvas=tk.Canvas(frame)
Mario=tk.PhotoImage(file="images\mario.png")
Diamond=tk.PhotoImage(file="images\diamond.png")
colors=["red","yellow","blue","green","purple","pink"]
grid=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,0,0],
    [0,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,2,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,2,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
def drawGrid():
    y1=10
    y2=70
    x1=40
    x2=100
    for elements in range(len(grid)):
        for values in range(len(grid[elements])):
            x1=x2
            x2+=60
            if grid[elements][values]==0:
                canvas.create_rectangle(x1,y1,x2,y2,fill="white")
            elif grid[elements][values]==2:
                canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors))
                canvas.create_image(x2-27,y2-27,image=Diamond)
            else:
                canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors))
                canvas.create_image(x2-27,y2-27,image=Mario)
        y1=y2
        y2+=60
        x1=40
        x2=100
drawGrid()
def findRow(array):
    for row in range(len(array)):
        if 1 in array[row]:
            return row
def findCol(array):
    for row in range(len(array)):
        if 1 in array[row]:
            for col in range(len(array[row])):
                if array[row][col]==1:
                    return col
def moveRight(event):
    Row=findRow(grid)
    Col=findCol(grid)
    if Col+1< len(grid[Row]):
        grid[Row][Col]=0
        grid[Row][Col+1]=1
    drawGrid()

def moveLeft(event):
    Row=findRow(grid)
    Col=findCol(grid)
    if Col>0:
        grid[Row][Col]=0
        grid[Row][Col-1]=1
    drawGrid()

def moveUp(event):
    Row=findRow(grid)
    Col=findCol(grid)
    if Row>0:
        grid[Row][Col]=0
        grid[Row-1][Col]=1
    drawGrid()
def moveDown(event):
    Row=findRow(grid)
    Col=findCol(grid)
    if Row+1< len(grid[Row]):
        grid[Row][Col]=0
        grid[Row+1][Col]=1
    drawGrid()
root.bind("<Down>",moveDown)
root.bind("<Up>",moveUp)
root.bind("<Left>", moveLeft)
root.bind('<Right>', moveRight)
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()