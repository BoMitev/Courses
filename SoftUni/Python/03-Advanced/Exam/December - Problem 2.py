def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


player_row, player_col = 0, 0
text = input()
matrix = []
size = int(input())
for r in range(size):
    line = list(input())
    matrix.append(line)
    for c in range(len(line)):
        if line[c] == "P":
            player_row, player_col = r, c

directions = {
    'right': lambda row, col: (row, col + 1),
    'left': lambda row, col: (row, col - 1),
    'up': lambda row, col: (row - 1, col),
    'down': lambda row, col: (row + 1, col),
}

for _ in range(int(input())):
    command = input()
    next_row, next_col = directions[command](player_row, player_col)
    if not is_inside(next_row, next_col, size):
        text = text[:-1]
        continue
    if matrix[next_row][next_col] != "-":
        text += matrix[next_row][next_col]
    matrix[player_row][player_col], matrix[next_row][next_col] = "-", matrix[player_row][player_col]
    player_row, player_col = next_row, next_col

print(text)
[print(''.join(matrix[r])) for r in range(len(matrix))]