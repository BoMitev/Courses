cards = input().split(":")
command = input().split()

while command[0] != "Ready":
    if command[0] == "Add":
        if command[1] not in cards:
            print("Card not found.")
        else:
            cards.append(command[1])
    elif command[0] == "Insert":

    command = input().split()