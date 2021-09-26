# You will be given an integer n for the size of the mines field with square shape and another one for the number of bombs that you have to place in the field. On the next n lines, you will receive the position for each bomb. Your task is to create the game field placing the bombs at the correct positions and mark them with "*", and calculate the numbers in each cell of the field. Each cell represents a number of all bombs directly near it (up, down, left, right and the 4 diagonals).     


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
