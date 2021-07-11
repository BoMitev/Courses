budget = int(input())
season = input()
fisherman = int(input())
discount = 0
price = 0

if fisherman <= 6:
    discount = 0.1
elif fisherman <= 11:
    discount = 0.15
else:
    discount = 0.25

if fisherman % 2 == 0 and season != "Autumn":
    discount += 0.05

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

total = price * (1 - discount)
difference = abs(budget - total)

if budget >= total:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
