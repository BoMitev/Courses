from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
water_bottle = [int(x) for x in input().split()]
wasted_water = 0

while len(cups_capacity) > 0 and len(water_bottle) > 0:
    for bottle in water_bottle[::-1]:
        current_cup = cups_capacity.popleft()
        water_bottle.pop()
        if bottle >= current_cup:
            bottle -= current_cup
        else:
            current_cup -= bottle
            cups_capacity.appendleft(current_cup)
            continue

        wasted_water += bottle
        if len(cups_capacity) == 0 or len(water_bottle) == 0:
            break

if len(cups_capacity) == 0:
    print(f"Bottles:", *water_bottle)
else:
    print(f"Cups:", *cups_capacity)
print(f"Wasted litters of water: {wasted_water}")