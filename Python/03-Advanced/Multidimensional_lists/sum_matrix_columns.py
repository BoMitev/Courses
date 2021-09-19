def read_matrix():
    rows, columns = map(int, input().split(", "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def get_column_sums(matrix):
    sums = []
    for c in range(len(matrix[0])):
        col_sum = 0
        for r in range(len(matrix)):
            col_sum += matrix[r][c]
        sums.append(col_sum)
    return sums


def print_result(values):
    [print(x) for x in values]


matrix = read_matrix()
result = get_column_sums(matrix)
print_result(result)
