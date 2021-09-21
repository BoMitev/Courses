def matrix_read():
    rows, columns = map(int, input().split())
    matrix = []
    for r in range(ord('a'), ord('a') + rows):
        row = []
        for c in range(columns):
            row.append(chr(r) + chr(r + c) + chr(r))
        matrix.append(row)
    return matrix


matrix = matrix_read()
for i in range(len(matrix)):
    print(' '.join(matrix[i]))