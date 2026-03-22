from turtle import *
from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
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


def check_winner():
    """Check if there is a winner."""
    lines = [
        # filas
        [(-200, -200), (-67, -200), (66, -200)],
        [(-200, -67), (-67, -67), (66, -67)],
        [(-200, 66), (-67, 66), (66, 66)],

        # columnas
        [(-200, -200), (-200, -67), (-200, 66)],
        [(-67, -200), (-67, -67), (-67, 66)],
        [(66, -200), (66, -67), (66, 66)],

        # diagonales
        [(-200, -200), (-67, -67), (66, 66)],
        [(-200, 66), (-67, -67), (66, -200)],
    ]

    for line in lines:
        values = [board.get(pos) for pos in line]

        if values[0] is not None and values.count(values[0]) == 3:
            return values[0]

    return None


players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    key = (x, y)

    # 🚫 Casilla ocupada
    if key in board:
        return

    player = state['player']
    draw = players[player]

    draw(x, y)
    update()

    board[key] = player

    # 🔍 Verificar ganador
    winner = check_winner()
    if winner is not None:
        print("Ganó:", "X" if winner == 0 else "O")
        return

    # 🤝 Verificar empate
    if len(board) == 9:
        print("Empate")
        return

    # 🔁 Cambiar turno
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
