import math
magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.5
cacti_price = 8

total = magnolias * magnolias_price + hyacinths * hyacinths_price + roses * roses_price\
    + cacti * cacti_price
tax = total * 0.05
profit = total - tax
difference = abs(profit - gift_price)

if profit >= gift_price:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")