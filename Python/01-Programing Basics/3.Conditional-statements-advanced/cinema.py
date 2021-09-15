project_type = input()
rows = int(input())
columns = int(input())
income = 0

premiere_price = 12
normal_price = 7.5
discount_price = 5
cinema_capacity = rows * columns

if project_type == "Premiere":
    income = cinema_capacity * premiere_price
elif project_type == "Normal":
    income = cinema_capacity * normal_price
elif project_type == "Discount":
    income = cinema_capacity * discount_price

print(f"{income:.2f} leva")