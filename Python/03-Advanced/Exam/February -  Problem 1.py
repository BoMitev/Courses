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
