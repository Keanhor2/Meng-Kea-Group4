
import tkinter as tk
root=tk.Tk()
# Adjust size
root.geometry("1820x700")
frame=tk.Frame()
canvas=tk.Canvas(frame)
#background interface-----------------------
bg = tk.PhotoImage(file = "images/My_bg.png")
canvas.create_image( 10, 20, image =bg)
# title of frame-----------------------
frame.master.title("Friends Help")
Mario=tk.PhotoImage(file="images\mario.png")
Diamond=tk.PhotoImage(file="images\purpleDiamond.png")
myEnemy=tk.PhotoImage(file="images\enemy.png")
# banner slide show -----------------
banner = tk.PhotoImage(file = "Images\Game.png")
canvas.create_image(0,0,image=banner,anchor="nw")
grid=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,3,0,0,0,0,0,2,0,0],
    [0,0,0,2,0,0,0,0,0,0],
    [0,0,0,3,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,3,0,0,0,0],
    [2,0,0,0,0,0,0,0,2,0],
    [0,0,0,0,0,0,0,3,0,0],
    [0,0,3,0,0,2,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

def drawGrid():
    canvas.delete("all")
    canvas.create_image( 0,0, image =bg)
    y1=15
    y2=75
    x1=10
    x2=110
    for elements in range(len(grid)):
        for values in range(len(grid[elements])):
            x1=x2
            x2+=100
            if grid[elements][values]==1:
                canvas.create_image(x2-55,y2-32,image=Mario,tags="play")
                
            elif grid[elements][values]==2:
                canvas.create_image(x2-50,y2-30,image=Diamond)
            else:
                canvas.create_rectangle(x1,y1,x2,y2,)
            
            if grid[elements][values]==0:
                canvas.create_rectangle(x1,y1,x2,y2,)
            elif grid[elements][values]==1:
                canvas.create_image(x2-55,y2-32,image=Mario)
            elif grid[elements][values]==2:
                canvas.create_image(x2-50,y2-30,image=Diamond)
            elif grid[elements][values]==3:
                canvas.create_image(x2-55,y2-32,image=myEnemy)
        y1=y2
        y2+=65
        x1=10
        x2=110

def deplay():
    drawGrid()
def displayButton():
    my_button = tk.Button(root,text="Play",command=deplay)
    my_button.config(width=7,height=1,bg="red",fg="yellow",font=("Arial",20,"bold"))
    my_button_canvas = canvas.create_window(650, 458, anchor = "nw", window =my_button,tags="button")
    # #button exit --------------------- 
    my_button = tk.Button(root,text="Exit",command=root.destroy)
    my_button.config(width=7,height=1,bg="red",fg="yellow",font=("Arial",20,"bold"))
    my_button_canvas = canvas.create_window(650, 520, anchor = "nw", window =my_button)
displayButton()

#find row ------------------------------------------------
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
def findRowOfEnemy(array):
    for row in range(len(array)):
        if 3 in array[row]:
            return row
def findColOfEnemy(array):
    for row in range(len(array)):
        if 3 in array[row]:
            for col in range(len(array[row])):
                if array[row][col]==3:
                    return col
#move right---------------------
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

def RightDiamond(event):
    global Score
    Row1=findRow(grid)
    Col1=findCol(grid)
    canvas.delete("all")
    if Col1+1< len(grid[Row1]):
        if grid[Row1][Col1+1] ==2:
            grid[Row1][Col1]=0
            grid[Row1][Col1+1]=1
            Score+=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    drawGrid()
#move left-----------------------
    print(Score)
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
def LeftDiamond(event):
    global Score
    Row1=findRow(grid)
    Col1=findCol(grid)
    canvas.delete("all")
    if Col1>0:
        if grid[Row1][Col1-1] ==2:
            grid[Row1][Col1]=0
            grid[Row1][Col1-1]=1
            Score+=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    drawGrid()
#move up------------------------------
    print(Score)
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
def UpDiamond(event):
    global Score
    Row1=findRow(grid)
    Col1=findCol(grid)
    canvas.delete("all")
    if Row1>0:
        if grid[Row1-1][Col1] ==2:
            grid[Row1][Col1]=0
            grid[Row1-1][Col1]=1
            Score+=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    drawGrid()
# move Down----------------------------
    print(Score)
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
    drawGrid()
    print(Score)
def DownDiamond(event):
    global Score
    Row1=findRow(grid)
    Col1=findCol(grid)
    canvas.delete("all")
    if Row1+1< len(grid[Row1]):
        if grid[Row1+1][Col1] ==2:
            grid[Row1][Col1]=0
            grid[Row1+1][Col1]=1
            Score+=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    drawGrid()
    print(Score)
root.bind("<Down>",moveDown)
root.bind("<Up>",moveUp)
root.bind("<Left>", moveLeft)
root.bind('<Right>', moveRight)
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()
