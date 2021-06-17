import math

b = input()
a = [x for x in b]
n = int(math.sqrt(len(a)))


def enter_cells(a):
    cells = []
    n = int(math.sqrt(len(a)))

    for i in range(n):
        cells.append([])
        for j in range(n):
            cells[i].append(a[i * n + j])
    return cells

cells = enter_cells(a)

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

print_cells(cells)

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

def replace_cell(cells, coordinates):
    cell = cells[coordinates[0]][coordinates[1]]

    if cell != '_':
       print('This cell is occupied! Choose another one!')
       return replace_cell(cells, turn())

    cells[coordinates[0]][coordinates[1]] = 'X'

replace_cell(cells, turn())
print_cells(cells)
