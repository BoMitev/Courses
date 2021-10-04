quantity = int(input())
days = int(input())
total_sum = 0
total_spirit = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for current_day in range(1, days+1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        total_sum += ornament_set_price * quantity
        total_spirit += 5
    if current_day % 3 == 0:
        total_sum += (tree_skirt_price + tree_garland_price) * quantity
        total_spirit += 13
    if current_day % 5 == 0:
        total_sum += tree_lights_price * quantity
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_sum += tree_skirt_price + tree_garland_price + tree_lights_price
if days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_sum}")
print(f"Total spirit: {total_spirit}")