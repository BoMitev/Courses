minutes = int(input())
times = int(input())
calories = int(input())

total_minutes = times * minutes
burned_calories = total_minutes * 5

if (calories / 2) <= burned_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
