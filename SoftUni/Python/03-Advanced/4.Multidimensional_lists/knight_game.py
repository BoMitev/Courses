def is_knight(board, row, col):
    size = len(board)
    if row < 0 or col < 0 or row >= size or col >= size:
        return False
    return board[row][col] == "K"


def count_affected_knights(board, row, col):
    result = 0
    if is_knight(board, row - 2, col - 1):
        result += 1
    if is_knight(board, row - 2, col + 1):
        result += 1
    if is_knight(board, row + 2, col - 1):
        result += 1
    if is_knight(board, row + 2, col + 1):
        result += 1
    if is_knight(board, row - 1, col - 2):
        result += 1
    if is_knight(board, row - 1, col + 2):
        result += 1
    if is_knight(board, row + 1, col - 2):
        result += 1
    if is_knight(board, row + 1, col+ 2):
        result += 1
    return result


size = int(input())
matrix = []
for _ in range(size):
    matrix.append(list(input()))

removed = 0
while True:
    max_count, k_row, k_col = 0, 0, 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == '0':
                continue
            count = count_affected_knights(matrix, r, c)
            if count > max_count:
                max_count, k_row, k_col = count, r, c
    if max_count == 0:
        break
    matrix[k_row][k_row] = "0"
    removed += 1

print(removed)
