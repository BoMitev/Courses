from collections import deque
def read_matrix():
    n = int(input())
    commands = deque(input().split())
    matrix = [input().split() for _ in range(n)]
    return matrix, commands


matrix, commands = read_matrix()
start_position = []
count = 0
is_finished = True
if len(start_position) == 0:
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "s":
                start_position = [r, c]

while commands:
    command = commands.popleft()
    next_position = []

    if command == "left":
        next_position = [start_position[0], start_position[1] - 1]
    elif command == "right":
        next_position = [start_position[0], start_position[1] + 1]
    elif command == "up":
        next_position = [start_position[0] - 1, start_position[1]]
    elif command == "down":
        next_position = [start_position[0] + 1, start_position[1]]

    if next_position[0] not in range(len(matrix)) or next_position[1] not in range(len(matrix[0])):
        next_position = start_position
    if matrix[next_position[0]][next_position[1]] == "c":
        matrix[next_position[0]][next_position[1]] = "*"
    elif matrix[next_position[0]][next_position[1]] == "e":
        is_finished = False
        break
    start_position = next_position

count = 0
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "c":
            count += 1

if not is_finished:
    print(f"Game over! ({', '.join(str(x) for x in next_position)})")
elif count > 0:
    print(f"{count} pieces of coal left. ({', '.join(str(x) for x in next_position)})")
else:
    print(f"You collected all coal! ({', '.join(str(x) for x in next_position)})")