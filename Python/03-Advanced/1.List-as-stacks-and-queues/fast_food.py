from collections import deque
quantity = int(input())
queue = deque()

for order in input().split():
    queue.append(int(order))

max = max(queue)

for i in range(len(queue)):
    order = queue.popleft()
    if order <= quantity:
        quantity -= order
    else:
        queue.appendleft(order)
        break

print(max)
if len(queue) > 0:
    print(f"Orders left: {' '.join(str(x) for x in queue)}")
else:
    print("Orders complete")