import math
numbers = input().split(", ")
numbers = [int(x) for x in numbers]
groups = math.ceil(max(numbers) / 10)
list = []
for group in range(1, groups+1):
    print(f"Group of {group * 10}'s: ", end="")
    for num in numbers:
        if (group*10)-10 < num <= group*10:
            list.append(num)
    print(list)
    list.clear()