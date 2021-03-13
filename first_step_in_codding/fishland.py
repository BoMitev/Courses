mackerel_price = float(input())
sprats_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

bonito_price = mackerel_price * 1.6
horse_mackerel_price = sprats_price * 1.8
mussels_price = 7.5

bonito_total = bonito_kg * bonito_price
hours_mackerel_total = horse_mackerel_kg * horse_mackerel_price
mussels_total = mussels_kg * mussels_price

total = bonito_total + hours_mackerel_total + mussels_total
print(f'{total:.2f}')
