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
canvas.create_image( 0, 0, image =bg)
frame.master.title("Friends Help")
Mario=tk.PhotoImage(file="images\mario.png")
Diamond=tk.PhotoImage(file="images\purpleDiamond.png")
banner = tk.PhotoImage(file = "Images\Game.png")
canvas.create_image(0,0,image=banner,anchor="nw")
# button start to play

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

def displayInterface(event):
    drawGrid()

def drawGrid():
    canvas.delete("all")
    canvas.create_image( 0, 0, image =bg)
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
number=0
def CollectDiamond():
    global number
    Row1=findRow(grid)
    Col1=findCol(grid)
    Row2=findRowDiamond(grid)
    Col2=findColDiamond(grid)
    if grid[Row1][Col1]==grid[Row2][Col2]:
        number+=1
        print(number)
    drawGrid()
#move right---------------------
def moveRight(event):
    Row=findRow(grid)
    Col=findCol(grid)
    canvas.delete("all")
    if Col+1< len(grid[Row]):
        grid[Row][Col]=0
        grid[Row][Col+1]=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    CollectDiamond()
    drawGrid()
#move left-----------------------
def moveLeft(event):
    Row=findRow(grid)
    Col=findCol(grid)
    canvas.delete("all")
    if Col>0:
        grid[Row][Col]=0
        grid[Row][Col-1]=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    CollectDiamond()
    drawGrid()
#move up------------------------------
def moveUp(event):
    Row=findRow(grid)
    Col=findCol(grid)
    canvas.delete("all")
    if Row>0:
        grid[Row][Col]=0
        grid[Row-1][Col]=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    CollectDiamond()
    drawGrid()
# move Down----------------------------
def moveDown(event):
    Row=findRow(grid)
    Col=findCol(grid)
    canvas.delete("all")
    if Row+1< len(grid[Row]):
        grid[Row][Col]=0
        grid[Row+1][Col]=1
    canvas.create_image( 0, 0, image =bg,anchor = "nw")
    CollectDiamond()
    drawGrid()
root.bind("<Button-1>",displayInterface)
root.bind("<Down>",moveDown)
root.bind("<Up>",moveUp)
root.bind("<Left>", moveLeft)
root.bind('<Right>', moveRight)
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()
