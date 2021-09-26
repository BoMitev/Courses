# You will be given an integer n for the size of the snake territory with square shape. On the next n lines, you will receive the rows of the territory. The snake will be placed on a random position, marked with the letter 'S'. On random positions there will be food, marked with '*'. There might also be a lair on the territory. The lair has two burrows. They are marked with the letter - 'B'. All of the empty positions will be marked with '-'.
# Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
# Move commands will be: "up", "down", "left", "right".
# If the snake moves to a food, it eats the food and increases the food quantity with one.
# If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear. If the snake goes out of its territory, it loses, can't return back and the program ends. The snake needs at least 10 food quantity to win.
# When the snake has gone outside of its territory or has eaten enough food, the game ends.


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
