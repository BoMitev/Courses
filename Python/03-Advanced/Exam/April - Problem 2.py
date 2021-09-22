# You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
# 1	2	3	4	5	6	7
# 24	D	D	D	D	D	8
# 23	D	T	T	T	D	9
# 22	D	T	B	T	D	10
# 21	D	T	T	T	D	11
# 20	D	D	D	D	D	12
# 19	18	17	16	15	14	13

# Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player. The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero or less wins the game.
# You are going to receive the information for every throw on a separate line. The coordinate information of a hit will be in the format: "({row}, {column})".
# •	If a player hits outside the dartboard, he does not score any points.
# •	If a player hits a number, it is deducted from his total.
# •	If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted from his total.
# •	If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted from his total.
# •	"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
# For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are deducted from his total.
# Your job is to find who won the game and with how many turns.


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
