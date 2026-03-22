from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    color("red")
    width(5)
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)


def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 17)  
    down()
    color("blue")
    width(5)
    circle(50)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
board = {}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    key = (x, y)

   
    if key in board:
        return

    player = state['player']
    draw = players[player]

    draw(x, y)
    update()
def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    key = (x, y)

    
    if key in board:
        return

    player = state['player']
    draw = players[player]

    draw(x, y)
    update()

    board[key] = player  

    state['player'] = not player
    board[key] = player  # guardar jugada

    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
