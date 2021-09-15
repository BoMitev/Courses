products = input().split("|")
command = input().split("%")

while command[0] != "Shop!":
    product = command[1]
    if command[0] == "Important":
        if product in products:
            products.remove(product)
            products.insert(0, product)
        else:
            products.insert(0, product)
    elif command[0] == "Add":
        if product not in products:
            products.append(product)
        else:
            print("The product is already in the list.")
    elif command[0] == "Swap":
        product_2 = command[2]
        if product in products:
            if product_2 in products:
                index_1 = products.index(product)
                index_2 = products.index(product_2)
                products[index_1], products[index_2] = products[index_2], products[index_1]
            else:
                print(f"Product {product_2} missing!")
        else:
            print(f"Product {product} missing!")
    elif command[0] == "Remove":
        if product in products:
            products.remove(product)
        else:
            print(f"Product {product} isn't in the list.")
    elif command[0] == "Reversed":
        products = [x for x in reversed(products)]
    command = input().split("%")
else:
    for i in range(len(products)):
        print(f"{i+1}. {products[i]}")
