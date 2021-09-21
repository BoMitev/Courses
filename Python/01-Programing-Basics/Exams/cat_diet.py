fat_percent = int(input())
protein_percent = int(input())
carbs_percent = int(input())
total_calories = int(input())
water_percent = int(input())

fat_grams = (total_calories * (fat_percent / 100)) / 9
protein_grams = (total_calories * (protein_percent /100)) / 4
carbs_grams = (total_calories * (carbs_percent / 100)) / 4
total_grams = fat_grams + protein_grams + carbs_grams
calories_per_gram = total_calories / total_grams
pure_calories = calories_per_gram * (1 - (water_percent / 100))

print(f"{pure_calories:.4f}")