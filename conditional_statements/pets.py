import math
days = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

dog_food = dog_food_per_day * days
cat_food = cat_food_per_day * days
turtle_food = turtle_food_per_day * days
total = dog_food + cat_food + turtle_food
difference = abs(food_left - total)

if food_left >= total:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")