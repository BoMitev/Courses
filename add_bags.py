luggage_over_20kg = float(input())
luggage_weight = float(input())
days_before_departure = int(input())
luggage_pcs = int(input())
luggage_price = 0

if luggage_weight < 10:
    luggage_price = luggage_over_20kg * 0.2
elif 10 <= luggage_weight <= 20:
    luggage_price = luggage_over_20kg * 0.5
else:
    luggage_price = luggage_over_20kg

if days_before_departure > 30:
    luggage_price *= 1.1
elif 7 <= days_before_departure <= 30:
    luggage_price *= 1.15
else:
    luggage_price *= 1.4

print(f"The total price of bags is: {luggage_price * luggage_pcs:.2f} lv.")