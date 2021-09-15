budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25
cozonac_price = flour_price + egg_price + milk_price
colored_eggs = 0
cozonacs_counter = 0

while budget - cozonac_price > 0:
    cozonacs_counter += 1
    budget -= cozonac_price
    colored_eggs += 3
    if cozonacs_counter % 3 == 0:
        colored_eggs -= cozonacs_counter - 2
print(f"You made {cozonacs_counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")