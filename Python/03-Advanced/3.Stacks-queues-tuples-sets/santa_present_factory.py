from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())
items = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
toys = []

while materials and magic_level:
    if materials[-1] == 0 or magic_level[0] == 0:
        if materials[-1] == 0:
            materials.pop()
        if magic_level[0] == 0:
            magic_level.popleft()
        continue

    material, magic = materials.pop(), magic_level.popleft()
    total = material * magic

    if total in items:
        toys.append(items[total])
    elif total < 0:
        materials.append(material + magic)
    elif total > 0:
        materials.append(material + 15)

if "Doll" in toys and "Wooden train" in toys or "Teddy bear" in toys and "Bicycle" in toys:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    materials_boxes = [str(n) for n in materials][::-1]
    print(f"Materials left: {', '.join(materials_boxes)}")

if magic_level:
    magic_values = [str(n) for n in magic_level]
    print(f"Magic left: {', '.join(magic_values)}")

unique_toys = set(toys)
for toy in sorted(unique_toys):
    print(f"{toy}: {toys.count(toy)}")