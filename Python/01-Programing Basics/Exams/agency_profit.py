air_company_name = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_ticket_price = float(input())
tax_price = float(input())

child_ticket_price = adult_ticket_price * 0.3
total_price = (adult_tickets * (adult_ticket_price + tax_price)) + (child_tickets * (child_ticket_price + tax_price))
profit = total_price * 0.2

print(f"The profit of your agency from {air_company_name} tickets is {profit:.2f} lv.")
