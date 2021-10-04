total = 0
tax = 0
discount = 1
price = input()

while price != "special":
    if price == "regular":
        break
    price = float(price)
    if price > 0:
        tax = tax + (price * 0.2)
        total += price
    else:
        print("Invalid price!")
    price = input()

if price == "special":
    discount = 0.9

if total > 0:
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          "-----------\n"
          f"Total price: {(tax + total) * discount:.2f}$")
else:
    print("Invalid order!")