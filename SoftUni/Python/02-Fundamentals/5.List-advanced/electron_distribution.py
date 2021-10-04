electrons = int(input())
index = 1
shells = []
while True:
    shell = 2 * index**2
    if shell < electrons:
        shells.append(shell)
        electrons -= shell
    else:
        shells.append(electrons)
        electrons = 0
    index += 1
    if electrons == 0:
        break
print(shells)
