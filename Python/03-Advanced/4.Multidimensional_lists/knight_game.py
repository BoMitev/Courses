def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = []
        for char in input():
            row.append(char)
        matrix.append(row)
    return matrix

matrix = read_matrix()
knights = []
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "K":
            knights.append(f"{r} {c}")

for knight in knights:
    row, col = knight.split()


print(*matrix, sep="\n")