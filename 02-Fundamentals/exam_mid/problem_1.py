orders = int(input())
total = 0

for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    count = int(input())
    coffee = (days * count) * price_per_capsule
    print(f"The price for the coffee is: ${coffee:.2f}")
    total += coffee

print(f"Total: ${total:.2f}")
