#On the first line, you will receive a sequence of pizza orders. Each order contains a different number of pizzas, separated by comma and space ", ". 
#On the second line, you will receive a sequence of employees with pizza-making capacities (how much pizzas an employee could make), separated by comma and space ", ".
#Your task is to check if all pizza orders are completed. 
#To do that, you should take the first order and the last employee and see:
    #•	If the number of pizzas in the order is less than or equal to the employee's pizza making capacity, the order is completed. Remove both the order and the employee.
    #•	If the number of pizzas in the order is greater than the employee's pizza making capacity, the remaining pizzas from the order are going to be made by the next employees until the order is completed. 
        #-If there are no more employees to finish the order, consider it not completed.
    #•	The restaurant does not take orders for more than 10 pizzas at once.
    #•	If an order is invalid (less than or equal to 0), you need to remove it before it is taken by an employee. 
#You should keep track of the total pizzas that are being made.

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
