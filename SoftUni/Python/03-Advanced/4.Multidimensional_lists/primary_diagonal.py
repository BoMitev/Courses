def read_matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


matrix = read_matrix()
sum = 0
for r in range(len(matrix)):
    sum += matrix[r][r]

print(sum)