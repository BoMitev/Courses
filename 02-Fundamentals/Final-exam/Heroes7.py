num = int(input())
dictionary = {}

for _ in range(num):
    name, hp, mana = input().split()
    if int(hp) > 100:
        hp = 100
    if int(mana) > 200:
        mana = 200
    dictionary[name] = {"health": int(hp), "mana": int(mana)}

command = input().split(" - ")
while command[0] != "End":
    hero_name = command[1]
    if command[0] == "CastSpell":
        needed_mana = int(command[2])
        spell = command[3]
        if dictionary[hero_name]["mana"] >= needed_mana:
            dictionary[hero_name]["mana"] -= needed_mana
            print(f"{hero_name} has successfully cast {spell} and now has {dictionary[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")
    elif command[0] == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        dictionary[hero_name]["health"] -= damage
        if dictionary[hero_name]["health"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dictionary[hero_name]['health']} HP left!")
        else:
            dictionary.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif command[0] == "Recharge":
        amount = int(command[2])
        if dictionary[hero_name]["mana"] + amount <= 200:
            charge = amount
        else:
            diff = (dictionary[hero_name]["mana"] + amount) - 200
            charge = amount - diff
        dictionary[hero_name]["mana"] += charge
        print(f"{hero_name} recharged for {charge} MP!")
    elif command[0] == "Heal":
        heal = int(command[2])
        if dictionary[hero_name]["health"] + heal <= 100:
            charge = heal
        else:
            diff = (dictionary[hero_name]["health"] + heal) - 100
            charge = heal - diff
        dictionary[hero_name]["health"] += charge
        print(f"{hero_name} healed for {charge} HP!")
    command = input().split(" - ")

for key, value in sorted(dictionary.items(), key=lambda x: (-x[1]['health'], x[0])):
    print(f"{key}\n  HP: {dictionary[key]['health']}\n  MP: {dictionary[key]['mana']}")