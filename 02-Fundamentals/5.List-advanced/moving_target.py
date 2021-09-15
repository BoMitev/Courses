targets = input().split()
targets = [int(x) for x in targets]
command = input().split()

while command[0] != "End":
    i = int(command[1])
    if command[0] == "Shoot":
        if 0 <= i < len(targets):
            targets[i] -= int(command[2])
            if targets[i] <= 0:
                targets.pop(i)
    elif command[0] == "Add":
        if 0 <= i < len(targets):
            targets.insert(i, int(command[2]))
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        area = targets[index-radius:index+radius+1]
        if len(area) < radius*2+1:
            print("Strike missed!")
        else:
            for x in area:
                targets.remove(x)
    command = input().split()
targets = [str(x) for x in targets]
print("|".join(targets))