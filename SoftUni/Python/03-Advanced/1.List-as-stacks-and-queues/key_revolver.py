from collections import deque

price_of_bullet = int(input())
size_of_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
bullet_count = 0
total_shots = 0

while locks:
    current_lock = locks.popleft()
    current_bullet = bullets.pop()
    bullet_count += 1
    total_shots += 1
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

    if bullet_count == size_of_barrel and len(bullets) > 0:
        print("Reloading!")
        bullet_count = 0
    elif len(bullets) == 0:
        break

if len(bullets) == 0 and len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
elif len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - (total_shots * price_of_bullet)}")