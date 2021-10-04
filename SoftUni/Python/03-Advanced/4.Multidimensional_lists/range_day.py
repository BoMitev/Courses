def is_inside(row, col):
    return 0 <= row < 5 and 0 <= col < 5


matrix = []
pos_row, pos_col = 0, 0
targets = 0
shoted_targets = 0
targets_positions = []

for r in range(5):
    text = input().split()
    matrix.append(text)
    for c in range(5):
        if text[c] == "A":
            pos_row, pos_col = r, c
        if text[c] == "x":
            targets += 1

directions = {
    'right': lambda row, col: (row, col + 1),
    'left': lambda row, col: (row, col - 1),
    'up': lambda row, col: (row - 1, col),
    'down': lambda row, col: (row + 1, col),
}

number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        for _ in range(steps):
            next_row, next_col = directions[direction](pos_row, pos_col)
            if not is_inside(next_row, next_col):
                next_row, next_col = pos_row, pos_col
            if matrix[next_row][next_col] == ".":
                matrix[pos_row][pos_col], matrix[next_row][next_col] = matrix[next_row][next_col], matrix[pos_row][pos_col]
                pos_row, pos_col = next_row, next_col
    if command[0] == "shoot":
        direction = command[1]
        next_row, next_col = directions[direction](pos_row, pos_col)
        while True:
            if not is_inside(next_row, next_col):
                break
            if matrix[next_row][next_col] == "x":
                shoted_targets += 1
                targets -= 1
                targets_positions.append([next_row, next_col])
                matrix[next_row][next_col] = "."
                break
            next_row, next_col = directions[direction](next_row, next_col)

    if targets == 0:
        break

if targets == 0:
    print(f"Training completed! All {shoted_targets} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
print(*targets_positions, sep="\n")