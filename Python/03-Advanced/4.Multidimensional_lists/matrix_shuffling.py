def matrix_read():
    rows, cols = map(int, input().split())
    matrix = []
    for r in range(rows):
        row = input().split()
        matrix.append(row)
    return matrix, rows, cols


matrix, rows, cols = matrix_read()
while True:
    command = input().split()
    if command[0] == "END":
        break

    if len(command) == 5 and all(int(i) >= 0 for i in command[1:]):
        pos1, pos2, pos3, pos4 = [int(x) for x in command[1:]]
        if pos1 not in range(len(matrix)) or pos2 not in range(len(matrix)) \
                or pos2 not in range(len(matrix[pos1])) or pos4 not in range(len(matrix[pos3])):
            print("Invalid input!")
            continue
    else:
        print("Invalid input!")
        continue

    if command[0] == "swap":
        matrix[pos1][pos2], matrix[pos3][pos4] = matrix[pos3][pos4], matrix[pos1][pos2]

    [print(' '.join(matrix[r])) for r in range(len(matrix))]
