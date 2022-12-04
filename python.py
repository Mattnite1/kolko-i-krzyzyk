import turtle
import time

def paintGrid():
    for a in range(3):
        moveTurtle(X + a*spaceBetweenSquares, Y)
        turtle.pendown()
        turtle.goto(X + a*spaceBetweenSquares, -Y)
        moveTurtle(X, Y - a*spaceBetweenSquares)
        turtle.pendown()
        turtle.goto(-X, Y - a*spaceBetweenSquares)

def orderXO():
    global orderInput
    if orderInput == 'kółko':
        orderInput = 'krzyżyk'
    else:
        orderInput = 'kółko'

def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)

def paintCharackter():
    if orderInput == 'krzyżyk':
        turtle.write("X", font=("Arial", 50))
    elif orderInput == 'kółko':
        turtle.write("O", font=("Arial", 50))
    else:
        turtle.clear()
        moveTurtle(-180, 80)
        turtle.write('Niewłaściwy', font=("Arial", 50, 'bold'))
        moveTurtle(-100, 0)
        turtle.write('kształt', font=("Arial", 50))
        moveTurtle(-120, -30)
        turtle.write('Wybierz między kółkiem, a krzyżykiem...', font=("Arial", 10, 'italic'))
        time.sleep(4)
        turtle.bye()

def checkWhoWin():
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

checkWinner = checkWhoWin
def moveTurtleAfterTheWin():
    moveTurtle(-240,0)
    turtle.clear()
    turtle.write("Wygrał: " + checkWinner(), font=("Arial", 50, 'bold'))
    time.sleep(3)
    turtle.bye()

moveTurtleAtEnd = moveTurtleAfterTheWin
def writeOutTheWinner():
    if checkWinner() == "kółko":
        moveTurtleAtEnd()
    elif checkWinner() == "krzyżyk":
        moveTurtleAtEnd()

def runGame(x, y):
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

    moveTurtle(centerOfColumn-25, centerOfRow-25)
    array[row][column] = orderInput

    paintCharackter()
    orderXO()
    writeOutTheWinner()

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

    paintGrid()
    orderInput = turtle.textinput("Wybierz", "kółko/krzyżyk")
    window.onclick(runGame)
    turtle.mainloop()
