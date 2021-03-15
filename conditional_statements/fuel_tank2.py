type_of_fuel = input()
volume = float(input())
discount_card = input()
price = 0

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

gasoline_discount = 0.18
diesel_discount = 0.12
gas_discount = 0.08

if type_of_fuel == "Gasoline":
    if discount_card == "Yes":
        price = (gasoline_price - gasoline_discount) * volume
    else:
        price = gasoline_price * volume

if type_of_fuel == "Diesel":
    if discount_card == "Yes":
        price = (diesel_price - diesel_discount) * volume
    else:
        price = diesel_price * volume

if type_of_fuel == "Gas":
    if discount_card == "Yes":
        price = (gas_price - gas_discount) * volume
    else:
        price = gas_price * volume

if 20 <= volume <= 25:
    price *= 0.92
elif volume > 25:
    price *= 0.9

print(f"{price:.2f} lv.")