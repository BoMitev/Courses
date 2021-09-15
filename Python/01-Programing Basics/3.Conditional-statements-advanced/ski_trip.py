days = int(input())
type_room = input()
feed = input()
price = 0

if type_room == "room for one person":
    price = 18
elif type_room == "apartment":
    price = 25
    if days < 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.5
elif type_room == "president apartment":
    price = 35
    if days < 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.8

if feed == "positive":
    price *= 1.25
elif feed == "negative":
    price *= 0.9

print(f"{price * (days - 1):.2f}")
