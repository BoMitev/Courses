from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
robots = []
available_robots = deque()
products = deque()

for el in data:
    robot_data = el.split("-")
    robot = {}
    robot['name'] = robot_data[0]
    robot['time'] = int(robot_data[1])
    robot['available'] = time
    available_robots.append(robot)
    robots.append(robot)

product = input()
while product != "End":
    products.append(product)
    product = input()

time += timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available'] = time + timedelta(seconds=current_robot['time'])
        robot = [x for x in robots if x == current_robot][0]
        robot['available'] = time + timedelta(seconds=current_robot['time'])
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r['available']:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot['available'] = time + timedelta(seconds=current_robot['time'])
            robot = [x for x in robots if x == current_robot][0]
            robot['available'] = time + timedelta(seconds=current_robot['time'])
            print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    time += timedelta(seconds=1)