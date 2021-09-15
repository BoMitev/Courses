gifts = input().split()

while True:
    command = input()
    cmd = command.split()
    if cmd[0] == "OutOfStock":
       for n in range(len(gifts)):
           if gifts[n] == cmd[1]:
               gifts[n] = "None"
    elif cmd[0] == "Required":
        num = int(cmd[2])
        if 0 < num < len(gifts):
            gifts[num] = cmd[1]
    elif cmd[0] == "JustInCase":
        gifts[-1] = cmd[1]
    elif command == "No Money":
        break

for x in gifts:
    if x != "None":
        print(x, end=" ")