def is_mine(board, row, col):
    if row < 0 or col < 0 or row >= len(board) or col >= len(board):
        return False
    return board[row][col] == "*"


def count_mines(board, row, col):
    result = 0
    if is_mine(board, row - 1, col):
        result += 1
    if is_mine(board, row - 1, col + 1):
        result += 1
    if is_mine(board, row, col + 1):
        result += 1
    if is_mine(board, row + 1, col + 1):
        result += 1
    if is_mine(board, row + 1, col):
        result += 1
    if is_mine(board, row + 1, col - 1):
        result += 1
    if is_mine(board, row, col - 1):
        result += 1
    if is_mine(board, row - 1, col - 1):
        result += 1
    return result


size = int(input())
bombs = int(input())
bomb_positions = [[int(n) for n in input()[1:-1].split(", ")] for _ in range(bombs)]
matrix = []
for r in range(size):
    row = []
    for c in range(size):
        if [r, c] in bomb_positions:
            row.append('*')
            continue
        row.append(' ')
    matrix.append(row)

for row in range(size):
    for col in range(size):
        if matrix[row][col] == " ":
            result = count_mines(matrix, row, col)
            matrix[row][col] = f"{result}"

[print(' '.join(matrix[r])) for r in range(len(matrix))]
