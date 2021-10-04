list = input().split()
bakery = {list[i]: int(list[i+1]) for i in range(0, len(list), 2)}
print(bakery)
