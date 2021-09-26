def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
food_quantity = 0
snake_row, snake_col = 0, 0
barrows = []
matrix = []
for r in range(size):
    field = list(input())
    matrix.append(field)
    for c in range(size):
        if field[c] == "S":
            snake_row, snake_col = r, c
        elif field[c] == "B":
           barrows.append([r, c])

directions = {
    'right': lambda row, col: (row, col + 1),
    'left': lambda row, col: (row, col - 1),
    'up': lambda row, col: (row - 1, col),
    'down': lambda row, col: (row + 1, col),
}

while True:
    command = input()
    next_row, next_col = directions[command](snake_row, snake_col)
    if not is_inside(next_row, next_col, size):
        matrix[snake_row][snake_col] = "."
        print("Game over!")
        break
    if matrix[next_row][next_col] == "*":
        food_quantity += 1
    elif matrix[next_row][next_col] == "B":
        matrix[next_row][next_col] = "."
        barrows.remove([next_row, next_col])
        next_barrow = barrows.pop()
        next_row, next_col = next_barrow[0], next_barrow[1]
    matrix[snake_row][snake_col], matrix[next_row][next_col] = ".", matrix[snake_row][snake_col]
    snake_row, snake_col = next_row, next_col
    if food_quantity == 10:
        break

if food_quantity >= 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")
[print(''.join(matrix[r])) for r in range(len(matrix))]