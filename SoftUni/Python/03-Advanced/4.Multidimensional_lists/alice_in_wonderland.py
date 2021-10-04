def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
matrix = []
alice_row, alice_col = 0, 0
for r in range(size):
    text = input().split()
    matrix.append(text)
    for c in range(size):
        if text[c] == "A":
            alice_row, alice_col = r, c

directions = {
    'right': lambda row, col: (row, col + 1),
    'left': lambda row, col: (row, col - 1),
    'up': lambda row, col: (row - 1, col),
    'down': lambda row, col: (row + 1, col),
}

tea_bags = 0
command = input()
matrix[alice_row][alice_col] = "*"
while command:
    alice_row, alice_col = directions[command](alice_row, alice_col)
    if not is_inside(alice_row, alice_col, size):
        break
    if matrix[alice_row][alice_col] == "R":
        matrix[alice_row][alice_col] = "*"
        break
    if matrix[alice_row][alice_col] != "." and matrix[alice_row][alice_col] != "*":
        tea_bags += int(matrix[alice_row][alice_col])
    matrix[alice_row][alice_col] = "*"
    if tea_bags >= 10:
        break
    command = input()

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(' '.join(matrix[r])) for r in range(len(matrix))]