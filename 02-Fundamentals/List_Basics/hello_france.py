items = input().split("|")
budget = int(input())
new_price = []
profit = 0
ticket = 0
for x in range(len(items)):
    type_price = items[x].split("->")
    if budget > 0:
        if type_price[0] == "Clothes" and float(type_price[1]) <= 50:
            if budget >= float(type_price[1]):
                budget -= float(type_price[1])
            else:
                continue
            new_price.append(float(type_price[1]) * 1.4)
            profit += float(type_price[1]) * 0.4
        elif type_price[0] == "Shoes" and float(type_price[1]) <= 35:
            if budget >= float(type_price[1]):
                budget -= float(type_price[1])
            else:
                continue
            new_price.append(float(type_price[1]) * 1.4)
            profit += float(type_price[1]) * 0.4
        elif type_price[0] == "Accessories" and float(type_price[1]) <= 20.50:
            if budget >= float(type_price[1]):
                budget -= float(type_price[1])
            else:
                continue
            new_price.append(float(type_price[1]) * 1.4)
            profit += float(type_price[1]) * 0.4
    else:
        break
for price in new_price:
    print(f"{price:.2f}", end=" ")
    ticket += int(price)
print(f"\nProfit: {profit:.2f}")
if ticket+budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")