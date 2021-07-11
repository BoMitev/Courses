num = int(input())
cabins = [int(x) for x in input().split() if 0 <= int(x) <= 4]
not_full = False

for i in range(0, len(cabins)):
    if cabins[i] < 4:
        seats_available = 4 - cabins[i]
        num -= seats_available
        cabins[i] = 4

        if num == 0:
            break
        elif num < 0:  # it would mean not all 4 seats are filled in current cabin
            cabins[i] = 4 + num  # as num is negative, seats in current cabin are reduced by num
            not_full = True
            break

if num > 0:
    print(f"There isn't enough space! {num} people in a queue!")
if not_full:
    print("The lift has empty spots!")

print(*cabins, sep=" ")