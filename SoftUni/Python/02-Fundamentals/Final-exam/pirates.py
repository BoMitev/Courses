dictionary = {}
command = input().split("||")
while command[0] != "Sail":
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in dictionary.keys():
        dictionary[city] = {"population": population, "gold": gold}
    else:
        dictionary[city]["population"] += population
        dictionary[city]["gold"] += gold
    command = input().split("||")

cmd = input().split("=>")
while cmd[0] != "End":
    town = cmd[1]
    if cmd[0] == "Plunder":
        people = int(cmd[2])
        gold = int(cmd[3])
        dictionary[town]["population"] -= people
        dictionary[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if dictionary[town]["population"] == 0 or dictionary[town]["gold"] == 0:
            dictionary.pop(town)
            print(f"{town} has been wiped off the map!")
    elif cmd[0] == "Prosper":
        gold = int(cmd[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            dictionary[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town]['gold']} gold.")
    cmd = input().split("=>")

if len(dictionary) > 0:
    print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
    for key, value in sorted(dictionary.items(), key=lambda x: (-x[1]["gold"], x[0])):
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")