n = int(input())
parking = {}
for i in range(n):
    command = input().split()
    func = command[0]
    username = command[1]
    if func == "register":
        plate = command[2]
        if username not in parking:
            parking[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking.get(username)}")
    elif func == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f"{username} unregistered successfully")

for k,v in parking.items():
    print(f"{k} => {v}")