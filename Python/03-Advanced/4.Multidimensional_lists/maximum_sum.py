from sys import maxsize


def read_matrix():
    rows, columns = map(int, input().split())
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def best_matrix():
    best_sum = -maxsize
    best_matrix = []
    for r in range(len(matrix) - 2):
        for c in range(len(matrix[r]) - 2):
            current_square = [matrix[r + x][c + y] for x in range(3) for y in range(3)]
            if sum(current_square) > best_sum:
                best_matrix.clear()
                best_sum = sum(current_square)
                best_matrix = current_square
    return (best_sum, best_matrix)


matrix = read_matrix()
best_sum, best_matrix = best_matrix()
print(f"Sum = {best_sum}")
for i in range(0, len(best_matrix), 3):
    print(f"{best_matrix[i]} {best_matrix[i+1]} {best_matrix[i+2]}")
