city = input()
amount = float(input())
commission = 0

if city == "Sofia":
    if 0 <= amount <= 500:
        commission = 0.05
    elif 500 < amount <= 1000:
        commission = 0.07
    elif 1000 < amount <= 10000:
        commission = 0.08
    elif amount > 10000:
        commission = 0.12
    else:
        print("error")
elif city == "Varna":
    if 0 <= amount <= 500:
        commission = 0.045
    elif 500 < amount <= 1000:
        commission = 0.075
    elif 1000 < amount <= 10000:
        commission = 0.1
    elif amount > 10000:
        commission = 0.13
    else:
        commisions = 0
elif city == "Plovdiv":
    if 0 <= amount <= 500:
        commission = 0.055
    elif 500 < amount <= 1000:
        commission = 0.08
    elif 1000 < amount <= 10000:
        commission = 0.12
    elif amount > 10000:
        commission = 0.145
    else:
        print("error")
else:
    print("error")

total = commission * amount
if total > 0:
    print(f"{commission * amount:.2f}")
