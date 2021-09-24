def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size

size = int(input())
matrix = []
bunny_row, bunny_col = 0, 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        if elements[col] == "B":
            bunny_row, bunny_col = row, col

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

max_eggs = float('-inf')
best_direction = ''
best_path = ''

for directions, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    path = []
    eggs = 0
    while True:
        current_row, current_col = step(current_row, current_col)
        if not is_inside(current_row, current_col, size):
            break

        if matrix[current_row][current_col] == "X":
            break

        path.append([current_row, current_col])
        eggs += int(matrix[current_row][current_col])
    if eggs > max_eggs:
        max_eggs = eggs
        best_direction = directions
        best_path = path

print(best_direction)
for step in best_path:
    print(step)
print(max_eggs)