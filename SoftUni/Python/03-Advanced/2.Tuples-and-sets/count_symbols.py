items = tuple(x for x in input())
items_set = set()

for i in items:
    items_set.add(f"{i}: {items.count(i)} time/s")

print('\n'.join(sorted(items_set)))