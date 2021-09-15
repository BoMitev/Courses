items = input().split(", ")
command = input().split()

while command[0] != "Craft!":
    if command[0] == "Collect":
        if command[2] not in items:
            items.append(command[2])
    elif command[0] == "Drop":
        if command[2] in items:
            items.remove(command[2])
    elif command[0] == "Combine" and command[1] == "Items":
        item = command[3].split(":")
        if item[0] in items:
            index = items.index(item[0])
            items.insert(index+1, item[1])
    elif command[0] == "Renew":
        if command[2] in items:
            items.remove(command[2])
            items.append(command[2])
    command = input().split()
print(", ".join(items))