import tkinter as tk
from tkinter.constants import END
import winsound
root = tk.Tk()
# Adjust size
# ===============Adjust size--------------------------
root.geometry("1820x700")
frame = tk.Frame()
canvas = tk.Canvas(frame)
# ==================background interface-----------------------
bg = tk.PhotoImage(file="images/My_bg.png")
canvas.create_image(0, 0, image=bg, anchor="nw")
# sound---------------------------------------------------

startMusic=winsound .PlaySound("Sound\StartGame.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
# ======================title of frame-----------------------
frame.master.title("Friends Help")
Mario = tk.PhotoImage(file="images\mario.png")
Diamond = tk.PhotoImage(file="images\purpleDiamond.png")
myEnemy = tk.PhotoImage(file="images\enemy.png")
# ======================banner slide show -----------------
banner = tk.PhotoImage(file="Images\Game.png")
canvas.create_image(0, 0, image=banner, anchor="nw")


# ------------------------Number 0 empty------------------------------------------
# ------------------------Number 1 Player------------------------------------------
# ------------------------Number 2 Diamond------------------------------------------
# ------------------------Number 3 Monster------------------------------------------

# grid of game-----------------------
grid = [
    [0, 0, 0, 0, 3, 1, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 3, 0, 3, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 2, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    [3, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 2, 0, 0, 0],
    [0, 3, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
]

# Function drawGrid---------------------------
def drawGrid():
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg,anchor="nw")
    y1 = 15
    y2 = 75
    x1 = 10
    x2 = 110
    for elements in range(len(grid)):
        for values in range(len(grid[elements])):
            x1 = x2
            x2 += 100
            if grid[elements][values] == 1:
                canvas.create_image(x2-55, y2-32, image=Mario, tags="play")
            elif grid[elements][values] == 2:
                canvas.create_image(x2-50, y2-30, image=Diamond)
            else:
                canvas.create_rectangle(x1, y1, x2, y2,)
            if grid[elements][values] == 0:
                canvas.create_rectangle(x1, y1, x2, y2,)
            elif grid[elements][values] == 1:
                canvas.create_image(x2-55, y2-32, image=Mario)
            elif grid[elements][values] == 2:
                canvas.create_image(x2-50, y2-30, image=Diamond)
            elif grid[elements][values] == 3:
                canvas.create_image(x2-55, y2-32, image=myEnemy)
                
        y1 = y2
        y2 += 65
        x1 = 10
        x2 = 110

# display interface ----------------------------------------------
def deplay():
    global startMusic
    drawGrid()
    startMusic=winsound .PlaySound("Sound\Click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

def displayButton():
    # button start to play
    my_button = tk.Button(root, text="Play", command=deplay)
    my_button.config(width=7, height=1, bg="#007EE9",fg="yellow",border="5", font=("Arial", 20, "bold"))
    canvas.create_window(630, 450, anchor="nw", window=my_button, tags="button")
#=====================================button exit ---------------------
    my_button = tk.Button(root, text="Exit", command=root.destroy)
    my_button.config(width=7, height=1, bg="#007EE9",fg="yellow",border="5",font=("Arial", 20, "bold"))
    canvas.create_window(630, 520, anchor="nw", window=my_button)
displayButton()
# ===================================find row ------------------------------------------------
def findRow(array):
    for row in range(len(array)):
        if 1 in array[row]:
            return row
def findCol(array):
    for row in range(len(array)):
        if 1 in array[row]:
            for col in range(len(array[row])):
                if array[row][col] == 1:
                    return col
def findRowDiamond(array):
    for row in range(len(array)):
        if 2 in array[row]:
            return row
def findColDiamond(array):
    for row in range(len(array)):
        if 2 in array[row]:
            for col in range(len(array[row])):
                if array[row][col] == 2:
                    return col
def findRowOfEnemy(array):
    for row in range(len(array)):
        if 3 in array[row]:
            return row
def findColOfEnemy(array):
    for row in range(len(array)):
        if 3 in array[row]:
            for col in range(len(array[row])):
                if array[row][col] == 3:
                    return col
def LostGame():
    canvas.create_text(660,300,text="Game Over!!",font=("",60),fill="red")
    LostGame()

# move right---------------------
Score = 0
def moveRight(event):
    global Score,startMusic
    Row1 = findRow(grid)
    Col1 = findCol(grid)
    canvas.delete("all")
    if Col1+1 < len(grid[Row1]) :
        if grid[Row1][Col1+1] ==0 :
            grid[Row1][Col1] = 0
            grid[Row1][Col1+1] = 1
            startMusic=winsound .PlaySound("Sound\walk.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif grid[Row1][Col1+1] == 2:
            startMusic=winsound .PlaySound("Sound\CatchDiamond.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[Row1][Col1] = 0
            grid[Row1][Col1+1] = 1
            Score += 1
        elif grid[Row1][Col1+1] == 3:
            startMusic=winsound .PlaySound("Sound\TouchMonster.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[Row1][Col1] = 0
            grid[Row1][Col1+1] = 1
            LostGame()
    drawGrid()
    print(Score)

# =================================move left-----------------------
def moveLeft(event):
    global Score,startMusic
    Row1 = findRow(grid)
    Col1 = findCol(grid)
    canvas.delete("all")
    if Col1 > 0 :
        if grid[Row1][Col1-1] == 0 :
            grid[Row1][Col1] = 0
            grid[Row1][Col1-1] = 1
            startMusic=winsound .PlaySound("Sound\walk.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif grid[Row1][Col1-1] == 2:
            startMusic=winsound .PlaySound("Sound\CatchDiamond.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[Row1][Col1] = 0
            grid[Row1][Col1-1] = 1
            Score += 1
        elif grid[Row1][Col1-1] == 3 :
            startMusic=winsound .PlaySound("Sound\TouchMonster.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[Row1][Col1] = 0
            grid[Row1][Col1-1] = 1
            LostGame()
    drawGrid()
    print(Score)

# move up------------------------------
# ===============================move up------------------------------
def moveUp(event):
    global Score,startMusic
    Row1 = findRow(grid)
    Col1 = findCol(grid)
    canvas.delete("all")
    if Row1 > 0 :
        if grid[Row1-1][Col1] == 0 :
            grid[Row1][Col1] = 0
            grid[Row1-1][Col1] = 1
            startMusic=winsound .PlaySound("Sound\walk.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif grid[Row1-1][Col1] == 2:
            startMusic=winsound .PlaySound("Sound\CatchDiamond.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[Row1][Col1] = 0
            grid[Row1-1][Col1] = 1
            Score += 1
        elif grid[Row1-1][Col1] == 3:
            startMusic=winsound .PlaySound("Sound\TouchMonster.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[Row1][Col1] = 0
            grid[Row1-1][Col1] = 1
            LostGame()
    drawGrid()
    print(Score)
# ==========================move Down----------------------------
def moveDown(event):
    global Score,startMusic
    Row1 = findRow(grid)
    Col1 = findCol(grid)
    canvas.delete("all")
    if Row1+1 < len(grid[Row1]):
        if grid[Row1+1][Col1] == 0 :
            grid[Row1][Col1] = 0
            grid[Row1+1][Col1] = 1
            startMusic=winsound .PlaySound("Sound\walk.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif grid[Row1+1][Col1] == 2:
            startMusic=winsound .PlaySound("Sound\CatchDiamond.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[Row1][Col1] = 0
            grid[Row1+1][Col1] = 1
            Score += 1
        elif grid[Row1+1][Col1] == 3 :
            startMusic=winsound .PlaySound("Sound\TouchMonster.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[Row1][Col1] = 0
            grid[Row1+1][Col1] = 1
            LostGame()
    drawGrid()
    print(Score)
root.bind("<Down>", moveDown)
root.bind("<Up>", moveUp)
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()
