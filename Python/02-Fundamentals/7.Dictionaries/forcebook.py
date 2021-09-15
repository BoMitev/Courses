forcebook = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        side, username = command.split(" | ")
        is_exist = False
        for values in forcebook.values():
                if username in values:
                    is_exist = True
        if side not in forcebook.keys() and not is_exist:
            forcebook[side] = []
            forcebook[side].append(username)
        elif not is_exist:
            forcebook[side].append(username)
    elif "->" in command:
        username, side = command.split(" -> ")
        is_exist = False
        for values in forcebook.values():
                if username in values:
                    is_exist = True
        if side not in forcebook.keys() and not is_exist:
            forcebook[side] = []
            forcebook[side].append(username)
        elif not is_exist:
            if side not in forcebook.keys():
                forcebook[side] = []
            forcebook[side].append(username)
        elif is_exist:
            for k,v in forcebook.items():
                if username in v:
                    forcebook[k].remove(v)
            if side not in forcebook.keys():
                forcebook[side] = []
            forcebook[side].append(username)
        print(f'{username} joins the {side} side!')
    command = input()

for k, v in sorted(forcebook.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for i in sorted(v):
            print(f"! {i}")