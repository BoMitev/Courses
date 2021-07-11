type = input()
sugar = input()
number = int(input())
price = 0

if type == "Espresso":
    if sugar == "Without":
        price = 0.9
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2
elif type == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6
elif type == "Tea":
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7

if sugar == "Without":
    price *= 0.65

if type == "Espresso" and number >= 5:
    price *= 0.75

total = price * number
if total > 15:
    price *= 0.8
final = price * number

print(f"You bought {number} cups of {type} for {final:.2f} lv.")