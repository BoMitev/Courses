health = 100
bitcoins = 0
count_rooms = 0
is_finished = True
rooms = input().split("|")

for x in rooms:
    command = x.split()
    number = int(command[1])
    count_rooms += 1
    if command[0] == "potion":
        amount = 100 - health
        health += number
        if health > 100:
            health = 100
            print(f"You healed for {amount} hp.")
        else:
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command[0] == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command[0]}.")
        else:
            print(f"You died! Killed by {command[0]}.")
            print(f"Best room: {count_rooms}")
            is_finished = False
            break

if is_finished:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")