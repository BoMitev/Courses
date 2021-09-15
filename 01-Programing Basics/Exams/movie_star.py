budget = float(input())
name = 0

while budget > 0:
    name = input()
    if name == "ACTION":
        break
    if len(name) > 15:
        salary = budget * 0.2
    else:
        salary = float(input())
    budget -= salary

if budget > 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")