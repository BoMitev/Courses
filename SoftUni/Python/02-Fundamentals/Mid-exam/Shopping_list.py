item_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    item = command[1]
    if command[0] == "Urgent":
        if item not in item_list:
            item_list.insert(0, item)
    elif command[0] == "Unnecessary":
        if item in item_list:
            item_list.remove(item)
    elif command[0] == "Correct":
        new_item = command[2]
        if item in item_list:
            index = item_list.index(item)
            item_list[index] = new_item
    elif command[0] == "Rearrange":
        if item in item_list:
            item_list.remove(item)
            item_list.append(item)
    command = input()
else:
    print(", ".join(item_list))