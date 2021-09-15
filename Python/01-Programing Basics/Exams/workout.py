import math
days = int(input())
first_day = float(input())
kilometers = first_day
total_range = first_day

for number in range(0, days):
    increasing_persentage = int(input()) / 100
    kilometers *= (1 + increasing_persentage)
    total_range += kilometers

if total_range >= 1000:
    print(f"You've done a great job running {math.ceil(total_range - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - total_range)} more kilometers")