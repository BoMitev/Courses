string = input().split(", ")
beggars = int(input())
beggars_list = []

for x in range(0, beggars):
    temp = string[x::beggars]
    for i in range(0, len(temp)):
        temp[i] = int(temp[i])
    beggars_list.append(sum(temp))

print(beggars_list)