import tkinter as tk
root=tk.Tk()
# Adjust size
root.geometry("1820x700")
frame=tk.Frame()
canvas=tk.Canvas(frame)
# Create Canvas
canvas =tk.Canvas( root, width = 900,height = 900)
# Add image file
bg = tk.PhotoImage(file = "images/My_bg.png")
# Display image
canvas.create_image( 0, 0, image =bg,anchor = "nw")
# canvas.pack(fill = "both", expand = True)
# frame.master.title("Friends Help")
Mario=tk.PhotoImage(file="images\mario.png")
Diamond=tk.PhotoImage(file="images\purpleDiamond.png")
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
# mario= canvas.create_image(55,32,image=Mario)
def drawGrid():
    y1=15
    y2=75
    x1=10
    x2=110
    for elements in range(len(grid)):
        for values in range(len(grid[elements])):
            x1=x2
            x2+=100
            if grid[elements][values]==0:
                canvas.create_rectangle(x1,y1,x2,y2,outline="")
            elif grid[elements][values]==2:
                canvas.create_image(x2-50,y2-30,image=Diamond)
            else:
                canvas.create_image(x2-55,y2-32,image=Mario)
        y1=y2
        y2+=65
        x1=10
        x2=110
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
        grid[Row][Col+1]=1 
        grid[Row][Col]=0
    drawGrid()
    # canvas.move(mario,20,0)

def moveLeft(event):
    Row=findRow(grid)
    Col=findCol(grid)
    if Col>0:
        grid[Row][Col-1]=1
        grid[Row][Col]=0
    drawGrid()
    # canvas.move(mario,-20,0)

def moveUp(event):
    Row=findRow(grid)
    Col=findCol(grid)
    if Row>0:
        grid[Row-1][Col]=1
        grid[Row][Col]=0
    drawGrid()
    # canvas.move(mario,0,-20)
def moveDown(event):
    Row=findRow(grid)
    Col=findCol(grid)
    if Row+1< len(grid[Row]):
        grid[Row+1][Col]=1
        grid[Row][Col]=0
    # canvas.move(mario,0,20)
    drawGrid()
root.bind("<Down>",moveDown)
root.bind("<Up>",moveUp)
root.bind("<Left>", moveLeft)
root.bind('<Right>', moveRight)
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()