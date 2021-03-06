from collections import deque

working_bees = deque([int(n) for n in input().split()])
nectar = deque([int(n) for n in input().split()])
process_symbols = deque(input().split())
total_honey = 0
while working_bees and nectar:
    bee, current_load = working_bees.popleft(), nectar.pop()
    while current_load < bee and nectar:
        current_load = nectar.pop()

    if current_load < bee:
        working_bees.appendleft(bee)
        break

    symbol = process_symbols.popleft()
    if symbol != "/":
        total_honey += abs(eval(f"{bee}{symbol}{current_load}"))
    else:
        if bee != 0 or current_load != 0:
            total_honey += abs(bee / current_load)

print(f"Total honey made: {total_honey}")
if working_bees:
    working_bees = [str(n) for n in working_bees]
    print(f"Bees left: {', '.join(working_bees)}")
if nectar:
    nectar = [str(n) for n in nectar]
    print(f"Nectar left: {', '.join(nectar)}")