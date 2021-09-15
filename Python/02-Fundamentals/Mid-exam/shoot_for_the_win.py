targets = [int(x) for x in input().split()]
command = input()
count = 0

while command != "End":
    index = int(command)
    if 0 <= index < len(targets):
        count += 1
        target = targets[index]
        targets[index] = -1
        for i in range(len(targets)):
            if targets[i] > target and targets[i] != -1:
                targets[i] -= target
            elif targets[i] <= target and targets[i] != -1:
                targets[i] += target
    command = input()
else:
    targets = [str(x) for x in targets]
    print(f"Shot targets: {count} -> " + " ".join(targets))