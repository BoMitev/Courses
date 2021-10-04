n = int(input())
items = set()

for _ in range(n):
    data = input().split()
    for i in data:
        items.add(i)

print("\n".join(items))