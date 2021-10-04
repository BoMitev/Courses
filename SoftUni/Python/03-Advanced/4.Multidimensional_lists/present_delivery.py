def cookies(matrix, row, col):
    happy_presents = 0
    all = 0
    if matrix[row + 1][col] != "S" and matrix[row + 1][col] != "-":
        if matrix[row + 1][col] == "V":
            happy_presents += 1
        all += 1
        matrix[row + 1][col] = '-'
    if matrix[row - 1][col] != "S" and matrix[row - 1][col] != "-":
        if matrix[row - 1][col] == "V":
            happy_presents += 1
        all += 1
        matrix[row - 1][col] = '-'
    if matrix[row][col + 1] != "S" and matrix[row][col + 1] != "-":
        if matrix[row][col + 1] == "V":
            happy_presents += 1
        all += 1
        matrix[row][col + 1] = '-'
    if matrix[row][col - 1] != "S" and matrix[row][col - 1] != "-":
        if matrix[row][col - 1] == "V":
            happy_presents += 1
        all += 1
        matrix[row][col - 1] = '-'
    return happy_presents, all


presents = int(input())
happy_presents = 0
size = int(input())
santa_row, santa_col = 0, 0
matrix = []
for row in range(size):
    field = input().split()
    matrix.append(field)
    for col in range(len(field)):
        if field[col] == "S":
            santa_row, santa_col = row, col

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

while happy_presents < presents:
    command = input()
    if command == "Christmas morning":
        break
    next_row, next_col = directions[command](santa_row, santa_col)
    if matrix[next_row][next_col] == "V":
        happy_presents += 1
        presents -= 1
    elif matrix[next_row][next_col] == "C":
        happy, all = cookies(matrix, next_row, next_col)
        happy_presents += happy
        presents -= all

    matrix[next_row][next_col] = "-"
    matrix[next_row][next_col], matrix[santa_row][santa_col] = matrix[santa_row][santa_col], matrix[next_row][next_col]
    santa_row, santa_col = next_row, next_col

happy_kids_left = 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "V":
            happy_kids_left += 1

if presents < happy_kids_left:
    print(f"Santa ran out of presents!")
[print(' '.join(matrix[r])) for r in range(len(matrix))]
if happy_kids_left == 0:
    print(f"Good job, Santa! {happy_presents} happy nice kid/s.")
else:
    print(f"No presents for {happy_kids_left} nice kid/s.")