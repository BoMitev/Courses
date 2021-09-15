lines = int(input())
capacity = 0

for i in range(lines):
    liters = int(input())
    capacity += liters
    if capacity > 255:
        capacity -= liters
        print("Insufficient capacity!")
        continue
print(capacity)