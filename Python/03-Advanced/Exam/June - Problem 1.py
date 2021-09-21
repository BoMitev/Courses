# You will be given two sequences of integers, representing bomb effects and bomb casings.
# You need to start from the first bomb effect and try to mix it with the last bomb casing. If the sum of their values
# is equal to any of the materials in the table below – create the bomb corresponding to the value and remove both bomb
# materials. Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you have no
# more bomb effects or bomb casings, or you successfully filled the bombs pouch.
# Bombs:
# •	Datura Bombs: 40
# •	Cherry Bombs: 60
# •	Smoke Decoy Bombs: 120
# To fill the bomb pouch, Ezio needs three of each of the bomb types.

from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casing = [int(x) for x in input().split(", ")]
bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
is_finished = False

while bomb_effects and bomb_casing:
    effect = bomb_effects.popleft()
    casing = bomb_casing.pop()

    if effect+casing == 40:
        bombs["Datura Bombs"] += 1
    elif effect+casing == 60:
        bombs["Cherry Bombs"] += 1
    elif effect+casing == 120:
        bombs["Smoke Decoy Bombs"] += 1
    else:
        bomb_effects.appendleft(effect)
        bomb_casing.append(casing-5)

    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        is_finished = True
        break

if not is_finished:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print(f"Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing)}")
else:
    print("Bomb Casings: empty")

for k,v in sorted(bombs.items(), key=lambda x: x[0]):
    print(f"{k}: {v}")