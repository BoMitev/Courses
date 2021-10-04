line_one = input().split()
line_two = input().split()
line_tree = input().split()
won = 0
line_one = [int(x) for x in line_one]
line_two = [int(x) for x in line_two]
line_tree = [int(x) for x in line_tree]
for x in range(len(line_one)):
    if line_one[x] == line_two[x] == line_tree[x]:
        if line_one[x] == 1:
            won = "First"
        elif line_one[x] == 2:
            won = "Second"

if all(line_one):
    if line_one[0] == 1:
        won = "First"
    elif line_one[0] == 2:
        won = "Second"

if all(line_two):
    if line_two[0] == 1:
        won = "First"
    elif line_two[0] == 2:
        won = "Second"

if all(line_tree):
    if line_tree[0] == 1:
        won = "First"
    elif line_tree[0] == 2:
        won = "Second"

if line_one[0] == line_two[1] == line_tree[2]:
    if line_one[0] == 1:
        won = "First"
    elif line_one[0] == 2:
        won = "Second"

if line_one[2] == line_two[1] == line_tree[0]:
    if line_one[2] == 1:
        won = "First"
    elif line_one[2] == 2:
        won = "Second"

if won == 0:
    print("Draw!")
else:
    print(f"{won} player won")