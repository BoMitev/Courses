def is_inside(row, col):
    return 0 <= row < 6 and 0 <= col < 6


def read_matrix():
    matrix = []
    for _ in range(6):
        matrix.append([int(x) if x.isdigit() else x for x in input().split()])
    return matrix


def sum_column(matrix, col):
    total = 0
    for row in range(len(matrix)):
        if isinstance(matrix[row][col], int):
            total += matrix[row][col]
    return total


import re


attempts = 3
points = 0
matrix = read_matrix()

for _ in range(attempts):
    target = re.search(r"\((?P<row>-*\d+), (?P<col>-*\d+)\)", input())
    row, col = int(target.group("row")), int(target.group("col"))
    if is_inside(row, col):
        if matrix[row][col] == "B":
            points += sum_column(matrix, col)
            matrix[row][col] = "b"

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
