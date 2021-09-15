goals = 0
table = {}
while goals < 10:
    player = input()
    if player != 'END':
        goals = int(input())
        table[player] = goals
    else:
        break
best_player = max(table, key=table.get)
goals = max(table.values())

print(f"{best_player} is the best player!")
if goals >= 3:
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")
