import pyautogui as pyg
import time
import copy
import keyboard

#PyAutoGUI Needs the Sudoku to be visible by setting sleep for 2 second it allows time to switch screen if needed
time.sleep(0.2)
#Initialize Array to store Sudoku 
sudoku =    [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#Defines the location of the top left cell and bottom right cell
topleftx = 914
toplefty = 390
brightx = 1287
brighty = 757
#Defines the size of the cell
boxw = (brightx - topleftx)/8
boxh = (brighty - toplefty)/8

#To fill the sudoku array from zero to numbers
def fill(nr, pos):
    global sudoku
    indexlx = int((pos[0] - topleftx + boxw/2)//boxw)
    indexly = int((pos[1] - toplefty + boxh/2)//boxw)
    sudoku[indexly][indexlx] = nr

#To fill the cell on the website with the correct number
def fillcell(nr, x, y):
    pyg.PAUSE = 0.01 #Lowers delay of pyautogui between actions
    xcoord = topleftx + boxw * x
    ycoord = toplefty + boxh * y
    pyg.click(xcoord, ycoord)
    pyg.press(str(nr))

#Path of the Numbers used to Compared to Screen
filepath = r'D:/Downloads/Project/Python/Sudoku/'
for i in range(1, 10):
    for pos in pyg.locateAllOnScreen(filepath+str(i)+'.png', grayscale=True, confidence=0.9):
        fill(i, pos)

#Prints out the array in a neat format
def printsudoku():
    print("\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)
    print("\n")

##Alogrithm to Solve Sudoku ===============

#Find the cell thats equal to 0 (empty)
def findNextCell(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1

#Check if matches the constraint of Sudoku
def isValid(sudoku, i, j, n):
    rowGood = all([n != sudoku[i][x] for x in range (9)]) #Checks if no numbers match in same row
    if rowGood:
        columnGood = all([n != sudoku[x][j] for x in range (9)]) #Checks if no number matches in same column
        if columnGood:
            TopX, TopY = 3*(i//3), 3*(j//3)
            for x in range(TopX, TopX+3): #Checks what is a possible number to fit
                for y in range (TopY, TopY+3):
                    if sudoku[x][y] == n:
                        return False
            return True
    return False

#Solve while checking if the number is in a valid location
def solveSudoku(sudoku, i=0, j=0):
    i, j = findNextCell(sudoku)
    if i == -1:
        return True

    for n in range(1, 10):
        if isValid(sudoku, i, j, n):
            sudoku[i][j] = n
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False

sudokucopy = copy.deepcopy(sudoku) #Creates a DeepCopy of the board which is used to compare the final outcome 
solveSudoku(sudoku)

windowselect = pyg.getWindowsWithTitle("Sudoku")[1] #something seems to cause solving to break
windowselect.activate()
    #Fills the cell on the site https://www.websudoku.com/?level=4
for x in range(9):
    for y in range(9):
        if sudokucopy[x][y] == 0:
            fillcell(sudoku[x][y], y, x)
        elif keyboard.is_pressed('esc'): #if the "q" key is pressed it quits the script
            quit()










