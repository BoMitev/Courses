def read_matrix():
    rows, columns = map(int, input().split(", "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix


def get_sum(matrix, row_i, col_i, size):
    the_sum = 0
    for r in range(row_i, row_i+size):
        for c in range(col_i, col_i+size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_submatrix(matrix, size):
    best_row = 0
    best_column = 0
    best_sum = get_sum(matrix, 0, 0, 2)

    for row in range(len(matrix) - 1):
        for col in range(len(matrix[row]) - 1):
            current_sum = get_sum(matrix, row, col, 2)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row = row
                best_column = col
    return (best_row, best_column)


def print_result(coordinates, size):
    (row_i, col_i) = coordinates
    for r in range(row_i, row_i + size):
        row = []
        for c in range(col_i, col_i + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum(matrix, row_i, col_i, 2))

matrix = read_matrix()
print_result(get_best_submatrix(matrix, 2), 2)