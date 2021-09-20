def read_matrix():
    rows, columns = map(int, input().split())
    matrix = []
    for i in range(rows):
        row = input().split()
        matrix.append(row)
    return matrix


matrix = read_matrix()
count = 0
for r in range(len(matrix)-1):
    for c in range(len(matrix[r])-1):
        if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
            count += 1
print(count)