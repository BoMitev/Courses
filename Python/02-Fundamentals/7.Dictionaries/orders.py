products = {}
command = input()

while command != "buy":
    name, price, quantity = command.split()
    if name not in products:
        products[name] = {"price": 0, "quantity": 0}
    products[name]["price"] = float(price)
    products[name]["quantity"] += float(quantity)
    command = input()
else:
    for k,v in products.items():
        total = 1
        for p,q in v.items():
            total *= q
        print(f"{k} -> {total:.2f}")