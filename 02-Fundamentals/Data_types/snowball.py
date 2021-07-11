snowballs = int(input())
high_snow = 0
high_time = 0
high_quality = 0
high_value = 0

for i in range(snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > high_value:
        high_value = snowball_value
        high_snow = snowball_snow
        high_time = snowball_time
        high_quality = snowball_quality
print(f"{high_snow} : {high_time} = {int(high_value)} ({high_quality})")