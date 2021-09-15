import math
grape_area = int(input())
kg_grapes_per_square = float(input())
wine_needed = int(input())
workers = int(input())

kg_of_grapes = grape_area * kg_grapes_per_square
wine = (kg_of_grapes * 0.4) / 2.5
difference = abs(wine_needed - wine)

if wine_needed > wine:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(difference / workers)} liters per person.")
