sea_excursions = int(input())
mountain_excursions = int(input())
total_excursions = sea_excursions + mountain_excursions
profit = 0
type_excursion = 0

while type_excursion != "Stop":
    type_excursion = input()
    if type_excursion == "sea" and sea_excursions > 0:
        profit += 680
        sea_excursions -= 1
        total_excursions -= 1
    if type_excursion == "mountain" and mountain_excursions >0:
        profit += 499
        mountain_excursions -= 1
        total_excursions -= 1
    if total_excursions == 0:
        break

if total_excursions == 0:
    print("Good job! Everything is sold.")
print(f"Profit: {profit} leva.")