targets = [int(x) for x in input().split()]
indx = input()
counter = 0

def valid(ind, target):
    if 0 <= ind < len(target):
        return True
    return False


while indx != 'End':
    indx = int(indx)
    if valid(indx, targets):
        counter += 1
        target = targets[indx]
        targets[indx] = -1
        for i in range(len(targets)):
            if targets[i] > target and targets[i] != -1:
                targets[i] -= target
            elif targets[i] <= target and targets[i] != -1:
                targets[i] += target
    indx = input()
else:
    print(f'Shot targets: {targets.count(-1)} -> {" ".join([str(x) for x in targets])}')