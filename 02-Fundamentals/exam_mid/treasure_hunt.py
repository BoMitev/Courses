treasure = input().split("|")
stolen_items = []

while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    if command[0] == "Loot":
        item_list = command[1:]
        for item in item_list:
            if item not in treasure:
                treasure.insert(0, item)
    elif command[0] == "Drop":
        if int(command[1]) in range(len(treasure)):
            item = treasure.pop(int(command[1]))
            treasure.append(item)
        else:
            continue
    elif command[0] == "Steal":
        stolen_items = treasure[-int(command[1]):]
        treasure = treasure[:-int(command[1])]
        print(", ".join(stolen_items))

treasure_sum = sum(len(x) for x in treasure)
count = sum([treasure.count(x) for x in treasure])

if len(treasure):
    print(f"Average treasure gain: {(treasure_sum/count):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")