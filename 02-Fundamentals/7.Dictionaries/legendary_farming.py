def collect_material(key_materials_dict: dict, junk_materials: dict, material: str, qty: int):
    if material == "shards" or material == "fragments" or material == "motes":
        key_materials_dict[material] += qty
    else:
        if material not in junk_materials.keys():
            junk_materials[material] = qty
        else:
            junk_materials[material] += qty


key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
obtained = ""

while obtained == "":
    items = input().split()
    for i in range(0, len(items), 2):
        quantity = int(items[i])
        material = items[i+1].lower()

        collect_material(key_materials, junk, material, quantity)

        if key_materials['shards'] >= 250:
            obtained = "Shadowmourne"
            key_materials['shards'] -= 250
            break
        elif key_materials['fragments'] >= 250:
            obtained = "Valanyr"
            key_materials['fragments'] -= 250
            break
        elif key_materials['motes'] >= 250:
            obtained = "Dragonwrath"
            key_materials['motes'] -= 250
            break

print(f"{obtained} obtained!")
for k,v in sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{k}: {v}")
for k,v in sorted(junk.items(), key=lambda kvp: (kvp[0])):
    print(f"{k}: {v}")