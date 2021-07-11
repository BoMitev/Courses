number = input()
list = number.split()
reversed = []
for x in range(0, len(list)):
    x = int(list[x]) * -1
    reversed.append(x)
print(reversed)