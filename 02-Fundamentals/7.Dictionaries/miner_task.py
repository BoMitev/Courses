command = input()
resource = {}
while command != "stop":
    quantity = int(input())
    if command not in resource:
        resource[command] = 0
    resource[command] += quantity
    command = input()

for k,v in  resource.items():
    print(f"{k} -> {v}")