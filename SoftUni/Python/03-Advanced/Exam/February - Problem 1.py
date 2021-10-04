# First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another
# sequence of integers representing explosive power.
# You need to start from the first firework effect and try to mix it with the last explosive power. If the sum of their
# values is:
# •	divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
# •	divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
# •	divisible by both 3 and 5 – create Crossette firework and remove both materials
# Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix the
# same explosive power with the next firework effect.
# If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
# When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive
# power, you need to stop mixing.
# To make the perfect firework show, Maria needs 3 of each of the firework types.

from collections import deque

fireworks = deque(int(x) for x in input().split(", "))
explosives = deque(int(x) for x in input().split(", "))
palm_count = 0
willow_count = 0
crossette_count = 0

while fireworks:
    if not explosives:
        break
    firework = fireworks.popleft()
    explosive = explosives.pop()
    if firework <= 0:
        explosives.append(explosive)
        continue
    elif explosive <= 0:
        fireworks.appendleft(firework)
        continue

    total = firework + explosive
    if total % 3 == 0 and total % 5 != 0:
        palm_count += 1
    elif total % 5 == 0 and total % 3 != 0:
        willow_count += 1
    elif total % 5 == 0 and total % 3 == 0:
        crossette_count += 1
    else:
        firework -= 1
        fireworks.append(firework)
        explosives.append(explosive)

    if palm_count >= 3 and willow_count >= 3 and crossette_count >= 3:
        break

if palm_count >= 3 and willow_count >= 3 and crossette_count >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left:", end=" ")
    print(*fireworks, sep=", ")

if explosives:
    print(f"Explosive Power left:", end=" ")
    print(*explosives, sep=", ")

print(f"Palm Fireworks: {palm_count}\n"
      f"Willow Fireworks: {willow_count}\n"
      f"Crossette Fireworks: {crossette_count}")
