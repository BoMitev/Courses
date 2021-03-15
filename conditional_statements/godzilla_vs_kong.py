budget = float(input())
statists = int(input())
price = float(input())

decorate = budget * 0.1
if statists > 150:
    price *= 0.9
cloths_price = statists * price
total_price = decorate + cloths_price
difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Action! \n"
          f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print(f"Not enough money! \n"
          f"Wingard needs {difference:.2f} leva more.")