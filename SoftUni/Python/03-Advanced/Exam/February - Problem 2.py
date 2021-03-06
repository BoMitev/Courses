# On the first line, you will be given a number representing the size of the field with square shape. On the next few lines, you will be given a field with: 
# •	One player randomly placed in it and marked with symbol "P"
# •	Numbers for coins placed at different positions of the field
# •	Walls marked with "X".
# After the field state, you will be given commands for the players movement. Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it. 
# If the player goes out of the field or he hits a wall, he loses the game and his coins are reduced to 50% and rounded down to the next-lowest number. The program ends.
# Otherwise, the player has to collect at least 100 coins to win the game.
# For more clarifications see the examples below.


from math import floor


def read_matrix():
    matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(int(input()))]
    return matrix


matrix = read_matrix()
coins = 0
path = []
current_position = []
if len(current_position) == 0:
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "P":
                current_position = [r, c]

while coins <= 100:
    command = input()
    row, col = current_position[0], current_position[1]
    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1
    else:
        continue

    if row in range(len(matrix)) and col in range(len(matrix[0])) and matrix[row][col] != "X":
        coins += matrix[row][col]
        path.append([row, col])
        matrix[row][col] = "P"
    else:
        break
    current_position = [row, col]

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {floor(coins*0.5)} coins.")
print("Your path:")
for p in path:
    print(p)
