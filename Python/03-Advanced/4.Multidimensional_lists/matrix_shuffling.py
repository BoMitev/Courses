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
        pos1 = int(command[1])
        pos2 = int(command[2])
        pos3 = int(command[3])
        pos4 = int(command[4])
        if pos1 >= rows or pos3 >= rows or pos2 >= cols or pos4 >= cols:
            print("Invalid input!")
            continue
    else:
        print("Invalid input!")
        continue

    if command[0] == "swap":
        matrix[pos1][pos2], matrix[pos3][pos4] = matrix[pos3][pos4], matrix[pos1][pos2]

    [print(' '.join(matrix[r])) for r in range(len(matrix))]
