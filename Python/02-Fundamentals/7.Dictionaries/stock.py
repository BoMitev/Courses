list = input().split()
products = {list[i]: int(list[i+1]) for i in range(0, len(list), 2)}
search = input().split()

for product in search:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")