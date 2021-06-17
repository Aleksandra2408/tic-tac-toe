import math


def enter_cells(a):
    cells = []
    n = int(math.sqrt(len(a)))

    for i in range(n):
        cells.append([])
        for j in range(n):
            cells[i].append(a[i * n + j])
    return cells


def print_cells(cells):
    n = len(cells)
    print('-' * (2 * n + 3))
    line = '| '
    for i in range(n ** 2):
        if i % n == 2 and i != n ** 2 - 1:
            line = line + cells[int(i / n)][i % n] + ' |' + '\n' + '| '
        elif i == n * n - 1:
            line = line + cells[int(i / n)][i % n] + ' |'
        else:
            line = line + cells[int(i / n)][i % n] + ' '
    print(line)
    print('-' * (2 * n + 3))


def turn():
    coordinates = []
    for x in input('Enter the coordinates: ').split(' '):
        if x.isdigit():
            if (int(x) > 3) or (int(x) < 1):
                print('Coordinates should be from 1 to 3!')
                return turn()
            else:
                coordinates.append(int(x) - 1)
        else:
            print('You should enter numbers!')
            return turn()
    return coordinates


def replace_cell(cells, symbol, coordinates):
    cell = cells[coordinates[0]][coordinates[1]]

    if cell != '_':
        print('This cell is occupied! Choose another one!')
        return replace_cell(cells, symbol, turn())

    cells[coordinates[0]][coordinates[1]] = symbol


def check(cells):
    n = len(cells)
    rows = []
    cols = []
    diagonals = [[], []]
    for row in range(n):
        rows.append([])
        cols.append([])
        diagonals[0].append(cells[row][row])
        diagonals[1].append(cells[row][n - row - 1])
        for col in range(n):
            rows[row].append(cells[row][col])
            cols[row].append(cells[col][row])

    lines = []
    for row in rows:
        lines.append(row)
    for col in cols:
        lines.append(col)
    for diagonal in diagonals:
        lines.append(diagonal)

    u = 0
    x = 0
    z = 0
    for cell in cells:
        for b in cell:
            if b == '_':
                u = u + 1
            elif b == 'X':
                x = x + 1
            elif b == 'O':
                z = z + 1

    x_line = 0
    z_line = 0
    for elem in lines:
        if elem == ['X', 'X', 'X']:
            x_line = x_line + 1
        elif elem == ['O', 'O', 'O']:
            z_line = z_line + 1

    if (x_line + z_line > 1) or ((x - z) > 1) or ((z - x) > 1):
        print('Impossible')
        return False
    elif (x_line + z_line == 0) and (u > 0):
        return True
    elif x_line > 0:
        print('X wins')
        return False
    elif z_line > 0:
        print('O wins')
        return False
    else:
        print('Draw')
        return False


b = '_________'
a = [x for x in b]
n = int(math.sqrt(len(a)))
s = 'X'

cells = enter_cells(a)

print_cells(cells)

while check(cells):
    replace_cell(cells, s, turn())
    print_cells(cells)
    if s == 'X':
        s = 'O'
    else:
        s = 'X'
