num = int(input())
dictionary = {}

for _ in range(num):
    plant, rarity = input().split("<->")
    dictionary[plant] = {"rarity": int(rarity), "rate": []}

command = input().split()
while command[0] != "Exhibition":
    plant = command[1]
    if command[0] == "Rate:":
        rate = int(command[3])
        if plant in dictionary.keys():
            dictionary[plant]["rate"].append(rate)
        else:
            print("error")
    elif command[0] == "Update:":
        new_rarity = int(command[3])
        if plant in dictionary.keys():
            dictionary[plant]["rarity"] = new_rarity
        else:
            print("error")
    elif command[0] == "Reset:":
        if plant in dictionary.keys():
            dictionary[plant]["rate"].clear()
        else:
            print("error")
    command = input().split()

for key, value in dictionary.items():
    if len(dictionary[key]["rate"]) > 0:
        average = sum(dictionary[key]["rate"])/len(dictionary[key]["rate"])
    else:
        average = 0
    dictionary[key]["rate"] = average

print(f"Plants for the exhibition:")
for key, value in sorted(dictionary.items(), key=lambda x: (-x[1]["rarity"], -x[1]["rate"])):
    print(f"- {key}; Rarity: {dictionary[key]['rarity']}; Rating: {dictionary[key]['rate']:.2f}")
