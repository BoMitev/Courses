pirate_ship_status = [int(a) for a in input().split(">")]
war_ship_status = [int(a) for a in input().split(">")]
max_health = int(input())
command = input().split()

while command[0] != "Retire":
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(war_ship_status):
            war_ship_status[index] -= damage
            if war_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break
    elif command[0] == "Defend":
        index = int(command[1])
        end = int(command[2])
        damage = int(command[3])
        if 0 <= end < len(pirate_ship_status):
            pirate_ship_status[index:end+1] = [a-damage for a in pirate_ship_status[index:end+1]]
            if min(pirate_ship_status) <= 0:
                print("You lost! The pirate ship has sunken.")
                break
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health:
                pirate_ship_status[index] = max_health
    elif command[0] == "Status":
        repair_section = [s for s in pirate_ship_status if 20 > (s/max_health)*100]
        print(f"{len(repair_section)} sections need repair.")
    command = input().split()
else:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(war_ship_status)}")