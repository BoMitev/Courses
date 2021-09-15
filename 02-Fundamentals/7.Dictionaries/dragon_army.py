dragon_list = {}
types = []
num = int(input())

for _ in range(num):
    type, name, damage, health, armor = input().split()
    if damage == "null":
        damage = "45"
    if health == "null":
        health = "250"
    if armor == "null":
        armor = "10"
    id = damage + ":" + health + ":" + armor
    if name not in dragon_list.keys():
        dragon_list[name] = {type: id}
    if type not in types:
        types.append(type)
    if name in dragon_list.keys() and type in types:
        dragon_list[name][type] = id

for i in types:
    average_damage = 0
    average_health = 0
    average_armor = 0
    count = 0
    for k,v in sorted(dragon_list.items(), key=lambda x: x[0]):
        for g,j in v.items():
            if g == i:
                j = j.split(":")
                average_damage += int(j[0])
                average_health += int(j[1])
                average_armor += int(j[2])
                count += 1
    print(dragon_list)
    print(f"{i}::({round(average_damage/count, 2):.2f}/{round(average_health/count, 2):.2f}/"
          f"{round(average_armor/count, 2):.2f})")
    for key, value in sorted(dragon_list.items(), key=lambda x: x[0]):
        for x,y in value.items():
            if x == i:
                y = y.split(":")
                print(f"-{key} -> damage: {y[0]}, health: {y[1]}, armor: {y[2]}")
