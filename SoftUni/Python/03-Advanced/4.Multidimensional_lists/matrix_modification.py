from collections import deque


def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


matrix = read_matrix()
commands = deque(input().split())
while commands[0] != "END":
    command = commands.popleft()
    commands = [int(x) for x in commands]

    if commands[0] in range(len(matrix)) and commands[1] in range(len(matrix[0])):
        if command == "Add":
            matrix[commands[0]][commands[1]] += commands[2]
        elif command == "Subtract":
            matrix[commands[0]][commands[1]] -= commands[2]
    else:
        print('Invalid coordinates')

    commands = deque(input().split())

for r in range(len(matrix)):
    print(' '.join(str(x) for x in matrix[r]))
