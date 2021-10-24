from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())
gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    total = magic + material

    if total < 100:
        if total % 2 == 0:
            material *= 2
            magic *= 3
            total = magic + material
        else:
            total *= 2
    elif total > 499:
        total /= 2

    if 100 <= total <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= total <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= total <= 399:
        gifts["Gold"] += 1
    elif 400 <= total <= 499:
        gifts["Diamond Jewellery"] += 1

if gifts["Gemstone"] >= 1 and gifts["Porcelain Sculpture"] >= 1\
        or gifts["Gold"] >= 1 and gifts["Diamond Jewellery"] >= 1:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for p, v in sorted(gifts.items()):
    if gifts[p] > 0:
        print(f"{p}: {v}")