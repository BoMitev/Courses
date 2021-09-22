def read_matrix():
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    coordinates = [[int(x) for x in b.split(",")] for b in input().split()]
    return matrix, coordinates


matrix, coordinates = read_matrix()
for bomb in coordinates:
    row, col = bomb
    if matrix[row][col] <= 0:
        continue

    power = matrix[row][col]
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r in range(len(matrix)) and c in range(len(matrix[r])) and matrix[r][c] > 0:
                matrix[r][c] -= power

alive = []
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] > 0:
            alive.append(matrix[r][c])

print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")
[print(' '.join(str(x) for x in matrix[r])) for r in range(len(matrix))]

