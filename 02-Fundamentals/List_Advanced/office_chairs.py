rooms = int(input())
free_chairs = 0
is_not_full = True

for room in range(1, rooms+1):
    chair_visitors = input().split()
    if len(chair_visitors[0]) < int(chair_visitors[1]):
        difference = int(chair_visitors[1]) - len(chair_visitors[0])
        print(f"{difference} more chairs needed in room {room}")
        is_not_full = False
    else:
        free_chairs += len(chair_visitors[0]) - int(chair_visitors[1])

if is_not_full:
    print(f"Game On, {free_chairs} free chairs left")