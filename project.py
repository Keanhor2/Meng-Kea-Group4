from os import get_inheritable
import tkinter as tk
from tkinter import *
root=Tk()
# Adjust size
root.geometry("1820x700")
frame=Frame()
canvas=Canvas(frame)
# Create Canvas
canvas =Canvas( root, width = 900,height = 900)
# Add image file
bg = PhotoImage(file = "images/My_bg.png")
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
# mario= canvas.create_image(x2-55,y2-32,image=Mario)
def drawGrid():
    y1=15
    y2=75
    x1=10
    x2=110
    for elements in range(len(grid)):
        for values in range(len(grid[elements])):
            x1=x2
            x2+=100
            if grid[elements][values]==1:
                canvas.create_image(x2-55,y2-32,image=Mario)
                
            elif grid[elements][values]==2:
                canvas.create_image(x2-50,y2-30,image=Diamond)
            else:
                canvas.create_rectangle(x1,y1,x2,y2,)
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
def findRowDiamond(array):
    for row in range(len(array)):
        if 2 in array[row]:
            return row
def findColDiamond(array):
    for row in range(len(array)):
        if 2 in array[row]:
            for col in range(len(array[row])):
                if array[row][col]==2:
                    return col
Score=0
def moveRight(event):
    global Score
    Row1=findRow(grid)
    Col1=findCol(grid)
    canvas.delete("all")
    if Col1+1< len(grid[Row1]):
        if grid[Row1][Col1+1] ==0:
            grid[Row1][Col1]=0
            grid[Row1][Col1+1]=1
        elif grid[Row1][Col1+1] ==2:
            grid[Row1][Col1]=0
            grid[Row1][Col1+1]=1
            Score+=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    drawGrid()
    print(Score)
    # canvas.move(mario,20,0)

def moveLeft(event):
    global Score
    Row1=findRow(grid)
    Col1=findCol(grid)
    canvas.delete("all")
    if Col1>0:
        if grid[Row1][Col1-1] ==0:
            grid[Row1][Col1]=0
            grid[Row1][Col1-1]=1
        elif grid[Row1][Col1-1] ==2:
            grid[Row1][Col1]=0
            grid[Row1][Col1-1]=1
            Score+=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    drawGrid()
    print(Score)
    # canvas.move(mario,-20,0)
def moveUp(event):
    global Score
    Row1=findRow(grid)
    Col1=findCol(grid)
    canvas.delete("all")
    if Row1>0:
        if grid[Row1-1][Col1] ==0:
            grid[Row1][Col1]=0
            grid[Row1-1][Col1]=1
        elif grid[Row1-1][Col1] ==2:
            grid[Row1][Col1]=0
            grid[Row1-1][Col1]=1
            Score+=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    drawGrid()
    print(Score)
    # canvas.move(mario,0,-20)
def moveDown(event):
    global Score
    Row1=findRow(grid)
    Col1=findCol(grid)
    canvas.delete("all")
    if Row1+1< len(grid[Row1]):
        if grid[Row1+1][Col1] ==0:
            grid[Row1][Col1]=0
            grid[Row1+1][Col1]=1
        elif grid[Row1+1][Col1] ==2:
            grid[Row1][Col1]=0
            grid[Row1+1][Col1]=1
            Score+=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    # canvas.move(mario,0,20)
    drawGrid()
    print(Score)

root.bind("<Down>",moveDown)
root.bind("<Up>",moveUp)
root.bind("<Left>", moveLeft)
root.bind('<Right>', moveRight)

canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()