def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."

    items = []
    for item, values in products.items():
        price, quantity = [float(x) for x in values]
        total = price * quantity

        if total <= budget:
            items.append(f"You bought {item} for {total:.2f} leva.")
            budget -= total

        if len(items) >= 5:
            break

    return '\n'.join(items)