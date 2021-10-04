from collections import deque

n = int(input())
stations = deque()

for _ in range(n):
    data = [int(x) for x in input().split()]
    stations.append(data)

tank = 0
not_passed = True
pump_to_start = 0

while not_passed:
    for pump in stations:
        if pump == stations[-1]:
            not_passed = False
            break
        fuel, distance = pump[:]
        if tank + fuel >= distance:
            tank += fuel
            tank -= distance
        else:
            pump_to_start += 1
            tank = 0
            stations.rotate(-1)
            break

print(pump_to_start)