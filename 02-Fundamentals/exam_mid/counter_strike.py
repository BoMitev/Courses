energy = int(input())
command = input()
count = 0
while command != "End of battle":
    distance = int(command)
    if energy - distance < 0:
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        break
    else:
        count += 1
        energy -= distance
        if count % 3 == 0:
            energy += count
    command = input()
else:
    print(f"Won battles: {count}. Energy left: {energy}")
