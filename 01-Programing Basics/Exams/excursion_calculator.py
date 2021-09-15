number_of_people = int(input())
season = input()
price = 0

if number_of_people > 5 and season == "spring":
    price = 48
elif number_of_people <= 5 and season == "spring":
    price = 50

if number_of_people > 5 and season == "summer":
    price = 45 * 0.85
elif number_of_people <= 5 and season == "summer":
    price = 48.5 * 0.85

if number_of_people > 5 and season == "autumn":
    price = 49.5
elif number_of_people <= 5 and season == "autumn":
    price = 60

if number_of_people > 5 and season == "winter":
    price = 85 * 1.08
elif number_of_people <= 5 and season == "winter":
    price = 86 * 1.08

print(f"{(price * number_of_people):.2f} leva.")