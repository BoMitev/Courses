import re


def read_matrix():
    matrix = []
    for _ in range(7):
        matrix.append([int(x) if x.isdigit() else x for x in input().split()])
    return matrix


def is_winning(scoreboard):
    for name in scoreboard:
        player = name[0]
        score = name[1]
        if score <= 0:
            return player
    return False


names = [[x, 501, 0] for x in input().split(", ")]
matrix = read_matrix()

while not is_winning(names):
    results = re.search(r"\((?P<row>-*\d+), (?P<col>-*\d+)\)", input())
    row, col = int(results.group("row")), int(results.group("col"))
    player = names.pop(0)

    if row in range(len(matrix)) and col in range(len(matrix[0])):
        if matrix[row][col] == "D":
            total = (matrix[0][col] + matrix[row][0] + matrix[-1][col] + matrix[row][-1]) * 2
        elif matrix[row][col] == "T":
            total = (matrix[0][col] + matrix[row][0] + matrix[-1][col] + matrix[row][-1]) * 3
        elif matrix[row][col] == "B":
            player[1] = 0
            player[2] += 1
            names.append(player)
            break
        else:
            total = matrix[row][col]
        player[1] -= total

    player[2] += 1
    names.append(player)

for player in names:
    name, score, trows = [x for x in player]
    if score <= 0:
        print(f"{name} won the game with {trows} throws!")
