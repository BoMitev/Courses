def get_next_position(direction, row, col):
    if direction == "U":
        return (row - 1, col)
    if direction == "D":
        return (row + 1, col)
    if direction == "L":
        return (row, col - 1)
    return (row, col + 1)


def is_inside(rows, cols, r, c):
    return 0 <= r < rows and 0 <= c < cols


def get_next_bunnies(bunnies, rows, cols):
    next_bunnies = []
    for r, c in bunnies:
        if is_inside(rows, cols, r - 1, c):
            next_bunnies.append([r - 1, c])
        if is_inside(rows, cols, r + 1, c):
            next_bunnies.append([r + 1, c])
        if is_inside(rows, cols, r, c - 1):
            next_bunnies.append([r, c - 1])
        if is_inside(rows, cols, r, c + 1):
            next_bunnies.append([r, c + 1])
    return next_bunnies


rows, cols = [int(x) for x in input().split()]
matrix = []
player_row = 0
player_col = 0

bunnies = []
for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(cols):
        el = row_elements[col]
        if el == 'P':
            player_row, player_col = row, col
        elif el == 'B':
            bunnies.append([row, col])

commands = input()
matrix[player_row][player_col] = "."
won = None
for command in commands:
    next_player_row, next_player_col = get_next_position(command, player_row, player_col)
    if not is_inside(rows, cols, next_player_row, next_player_col):
        won = True
    elif matrix[next_player_row][next_player_col] == 'B':
        won = False

    if not won:
        player_row, player_col = next_player_row, next_player_col

    next_bunnies = get_next_bunnies(bunnies, rows, cols)
    for r, c in next_bunnies:
        if r == player_row and c == player_col and not won:
            won = False
        matrix[r][c] = 'B'
    bunnies += next_bunnies
    if won is not None:
        break

for elements in matrix:
    print(''.join(elements))

if won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")