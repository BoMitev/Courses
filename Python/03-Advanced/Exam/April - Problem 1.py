from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employees = [int(x) for x in input().split(", ")]
total = 0

while pizza_orders and employees:
    if not 0 < pizza_orders[0] <= 10:
        pizza_orders.popleft()
        continue

    order, employer = pizza_orders.popleft(), employees.pop()
    if order <= employer:
        result = order
    else:
        left = order - employer
        result = employer
        pizza_orders.appendleft(left)
    total += result

if not pizza_orders:
    print("All orders are successfully completed!\n"
          f"Total pizzas made: {total}\n"
          f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print("Not all orders are completed.\n"
          f"Orders left: {', '.join(str(x) for x in pizza_orders)}")