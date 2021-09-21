import math
time_needed = int(input())
days = int(input())
workers_overtime = int(input())

pure_working_time = (days * 0.9) * 8
overtime = workers_overtime * (2 * days)
total_time = math.floor(pure_working_time + overtime)
difference = abs(time_needed - total_time)

if total_time >= time_needed:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")