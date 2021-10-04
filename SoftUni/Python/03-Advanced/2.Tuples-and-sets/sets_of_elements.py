n, m = [int(x) for x in input().split()]
set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(input())

for _ in range(m):
    set_m.add(input())

output = set_n.intersection(set_m)
print('\n'.join(output))