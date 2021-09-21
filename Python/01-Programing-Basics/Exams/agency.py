company_name = input()
tickets_adults = int(input())
tickets_children = int(input())
adult_price = float(input())
tax = float(input())

children_price = adult_price * 0.3
total = (tickets_adults * (adult_price + tax)) + (tickets_children * (children_price + tax))
profit = total * 0.2

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")