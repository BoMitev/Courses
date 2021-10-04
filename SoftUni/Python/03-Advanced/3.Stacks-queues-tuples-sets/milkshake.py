from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))
count = 0

while chocolates and milk_cups:
    if chocolates[-1] <= 0 or milk_cups[0] <= 0:
        if chocolates[-1] <= 0:
            chocolates.pop()
        if milk_cups[0] <= 0:
            milk_cups.popleft()
        continue

    choco, milk = chocolates.pop(), milk_cups.popleft()
    if choco == milk:
        count += 1
    else:
        milk_cups.append(milk)
        chocolates.append(choco-5)

    if count == 5:
        break

if count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate:", end=" ")
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk:", end=" ")
    print(*milk_cups, sep=", ")
else:
    print("Milk: empty")
