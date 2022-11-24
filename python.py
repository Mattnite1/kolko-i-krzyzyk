import turtle
import time

def orderXO():
    global orderInput
    if orderInput == 'kółko':
        orderInput = 'krzyżyk'
    else:
        orderInput = 'kółko'

def paintingOX():
    if orderInput == 'krzyżyk':
        turtle.write("X", font=("Arial", 50))
    elif orderInput == 'kółko':
        turtle.write("O", font=("Arial", 50))
    else:
        turtle.penup()
        turtle.goto(-280, 0)
        turtle.clear()
        turtle.write('Niepoprawny wzór', font=("Arial", 50))
        turtle.bye()

def checkingWhoWin():
    # rows for circle
    for w in range(3):
        if (array[w][0] == "kółko" and array[w][1] == "kółko" and array[w][2] == "kółko"):
            return array[w][2]

    # rows for cross
    for w in range(3):
        if (array[w][0] == "krzyżyk" and array[w][1] == "krzyżyk" and array[w][2] == "krzyżyk"):
            return array[w][2]

    # columns for circle
    for k in range(3):
        if (array[0][k] == "kółko" and array[1][k] == "kółko" and array[2][k] == "kółko"):
            return array[2][k]

    # columns for cross
    for k in range(3):
        if (array[0][k] == "krzyżyk" and array[1][k] == "krzyżyk" and array[2][k] == "krzyżyk"):
            return array[2][k]

    if array[0][0] == array[1][1] and array[0][0] == array[2][2]:
        return array[2][2]
    if array[0][2] == array[1][1] and array[0][2] == array[2][0]:
        return array[2][0]

checkingWinner = checkingWhoWin

def movingTurtleAfterTheWin():
    turtle.penup()
    turtle.goto(-250, 0)
    turtle.clear()
    turtle.write("Wygrały: " + checkingWinner(), font=("Arial", 50))

def writingOutTheWinner():
    if checkingWinner() == "kółko":
        movingTurtleAfterTheWin()
    elif checkingWinner() == "krzyżyk":
        movingTurtleAfterTheWin()

def runGame(x, y):
    column = 0
    row = 0

    if x < X + spaceBetweenSquares:
        column = 0
    elif x > X + 2*spaceBetweenSquares:
        column = 2
    else:
        column = 1

    if y < Y - 2*spaceBetweenSquares:
        row = 2
    elif y > Y - spaceBetweenSquares:
        row = 0
    else:
        row = 1

    if array[row][column] != None:
        return array

    centerOfColumn = (column*spaceBetweenSquares +
                      spaceBetweenSquares/2) - boardSide / 2
    centerOfRow = (-row*spaceBetweenSquares -
                   spaceBetweenSquares/2) + boardSide / 2

    turtle.penup()
    turtle.goto(centerOfColumn-25, centerOfRow-25)

    array[row][column] = orderInput

    paintingOX()
    orderXO()
    writingOutTheWinner()


if __name__ == "__main__":
    window = turtle.Screen()
    boardSide = 600
    X = -300
    Y = 300

    window.setup(boardSide, boardSide)
    window.title("Kółko i krzyżyk")
    window.bgcolor('black')

    turtle.color('white')
    turtle.pensize(7)
    turtle.speed(0)
    turtle.hideturtle()

    spaceBetweenSquares = int(boardSide / 3)

    array = [[None, None, None], [None, None, None], [None, None, None]]

    for a in range(3):
        turtle.penup()
        turtle.goto(X + a*spaceBetweenSquares, Y)
        turtle.pendown()
        turtle.goto(X + a*spaceBetweenSquares, -Y)

        turtle.penup()
        turtle.goto(X, Y - a*spaceBetweenSquares)
        turtle.pendown()
        turtle.goto(-X, Y - a*spaceBetweenSquares)

    orderInput = turtle.textinput("Wybierz", "kółko/krzyżyk")
window.onclick(runGame)
turtle.mainloop()
