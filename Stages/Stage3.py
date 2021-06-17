import math
b = input()
a = [x for x in b]
n = int(math.sqrt(len(a)))

print('-' * (2 * n + 3))
line = '| '
for i in range(len(a)):
    if i % n == 2 and i != len(a) - 1:
        line = line + a[i] + ' |' + '\n' + '| '
    elif i == len(a) - 1:
        line = line + a[i] + ' |'
    else:
        line = line + a[i] + ' '
print(line)
print('-' * (2 * n + 3))

rows = []
cols = []
diagonals = [[], []]
for row in range(n):
    rows.append([])
    cols.append([])
    diagonals[0].append(a[row * n + row])
    diagonals[1].append(a[row * (n - 1) + 2])
    for col in range(n):
        rows[row].append(a[row * n + col])
        cols[row].append(a[col * n + row])

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
for b in a:
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
elif (x_line + z_line == 0) and (u > 0):
    print('Game not finished')
elif x_line > 0:
    print('X wins')
elif z_line > 0:
    print('O wins')
else:
    print('Draw')

