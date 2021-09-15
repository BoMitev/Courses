from collections import deque

timer = green_timer = int(input())
free = free_window = int(input())
is_crashed = False
cars_queue = deque()
count = 0

command = input()
while command != "END":
    if command == "green":
        timer = green_timer
        free = free_window
        while cars_queue and not is_crashed:
            if timer > 0:
                current_car = cars_queue.popleft()
                count += 1
                for char in current_car:
                    if timer > 0:
                        timer -= 1
                    elif free > 0:
                        free -= 1
                    else:
                        print(f"A crash happened!\n{current_car} was hit at {char}.")
                        is_crashed = True
                        break
            else:
                break
    else:
        cars_queue.append(command)
    command = input()

if not is_crashed:
    print(f"Everyone is safe.\n{count} total cars passed the crossroads.")