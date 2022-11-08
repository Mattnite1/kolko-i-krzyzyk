from ctypes import sizeof
from pickle import NONE
import random
import turtle
import time

window = turtle.Screen()
side = 600
X = -300
Y = 300
window.setup(side, side)
window.title("Kolko i krzyżyk")
window.bgcolor('black')

turtle.color('white')
turtle.pensize(7)
turtle.speed(0)
turtle.hideturtle()

tablica = [[None, None, None],
            [None, None, None],
            [None, None, None]]

space = int(side / 3)

for a in [1, 2]:
    turtle.penup()
    turtle.goto(X + a*space, Y)
    turtle.pendown()
    turtle.goto(X + a*space, -Y)

    turtle.penup()
    turtle.goto(X, Y - a*space)
    turtle.pendown()
    turtle.goto(-X, Y - a*space)

orderInput = turtle.textinput("Wybierz", "kolko/krzyzyk")

def orderShapes():
    if orderInput == 'krzyzyk':
        turtle.write("X", font=("Arial", 50))
    elif orderInput == 'kolko':
        turtle.write("O", font=("Arial", 50))
    else:
        turtle.penup()
        turtle.goto(-280,0)
        turtle.clear()
        turtle.write('Niepoprawny wzór', font=("Arial", 50))
        turtle.bye()

def sequenceOfShapes():
    global orderInput
    if orderInput == 'kolko':
        orderInput = 'krzyzyk'
    else:
        orderInput = 'kolko'

def winCheck(): 

    #rows for circle
    for w in range(3):   
        if (tablica[w][0] != None and tablica[w][0] == "kolko" and tablica[w][1] != None and tablica[w][1] == "kolko" and tablica[w][2] != None and tablica[w][2] == "kolko"):   
            return tablica[w][2] 

    #rows for cross
    for w in range(3):
        if (tablica[w][0] != None and tablica[w][0] == "krzyzyk" and tablica[w][1] != None and tablica[w][1] == "krzyzyk" and tablica[w][2] != None and tablica[w][2] == "krzyzyk"):   
            return tablica[w][2] 
   
    #columns for circle
    for k in range(3):
        if (tablica[0][k] != None and tablica[0][k] == "kolko" and tablica[1][k] != None and tablica[1][k] == "kolko" and tablica[2][k] != None and tablica[2][k] == "kolko"):   
            return tablica[2][k] 
    
    #columns for cross 
    for k in range(3):
        if (tablica[0][k] != None and tablica[0][k] == "krzyzyk" and tablica[1][k] != None and tablica[1][k] == "krzyzyk" and tablica[2][k] != None and tablica[2][k] == "krzyzyk"):   
            return tablica[2][k]     


    if tablica[0][0] == tablica[1][1] and  tablica[0][0] == tablica[2][2]: return tablica[2][2]
    if tablica[0][2] == tablica[1][1] and  tablica[0][2] == tablica[2][0]: return tablica[2][0]

    #rysowanie

def writingOutTheWinner():   

    if winCheck() != None:
            turtle.penup()
            turtle.goto(-250,0)
            turtle.clear()
            if winCheck() == "kolko":
                turtle.penup()
                turtle.goto(-230,0)
                turtle.write("Wygrały: " + winCheck(), font=("Arial", 50))
            elif winCheck() == "krzyzyk":
                turtle.write("Wygrały: " + winCheck(), font=("Arial", 50))

def runGame(x, y):

    global orderInput
    column = 0
    row = 0

    if x < X + space: column = 0
    elif x > X + 2*space: column = 2
    else: column = 1

    if y < Y - 2*space: row = 2
    elif y > Y - space: row = 0
    else: row = 1
    
    if tablica[row][column] != None: return tablica

    centerOfColumn = (column*space + space/2) - side / 2
    centerOfRow = (-row*space - space/2) + side / 2
    
    turtle.penup()
    turtle.goto(centerOfColumn-25, centerOfRow-25)
    
    tablica[row][column] = orderInput

    orderShapes()
    sequenceOfShapes()
    writingOutTheWinner()
    
window.onclick(runGame)
turtle.mainloop()

