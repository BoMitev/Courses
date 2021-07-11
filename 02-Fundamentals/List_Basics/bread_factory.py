energy = 100
coins = 100
working_day = input().split("|")
is_completed = True

for x in range(len(working_day)):
    event = working_day[x].split("-")
    if event[0] == "rest":
        energy += int(event[1])
        if energy >= 100:
            gain = int(event[1]) - (energy - 100)
            energy = 100
        else:
            gain = int(event[1])
        print(f"You gained {gain} energy.")
        print(f"Current energy: {energy}.")
    elif event[0] == "order":
        if energy >= 30:
            energy -= 30
            coins += int(event[1])
            print(f"You earned {int(event[1])} coins.")
        else:
            energy += 50
            if energy >= 100:
                energy = 100
            print(f"You had to rest!")
            continue
    else:
        if coins > int(event[1]):
            print(f"You bought {event[0]}.")
            coins -= int(event[1])
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            is_completed = False
            break
if is_completed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")