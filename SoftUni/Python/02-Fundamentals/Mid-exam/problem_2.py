parts = input().split("|")
command = input().split()

while command[0] != "Done":
    num = command[1]
    if command[0] == "Add":
        particle = command[1]
        index = int(command[2])
        if 0 <= index < len(parts):
            parts.insert(index, particle)
    elif command[0] == "Remove":
        index = int(command[1])
        if 0 <= index < len(parts):
            parts.pop(index)
    elif command[0] == "Check" and command[1] == "Even":
        even = []
        for i in range(len(parts)):
            if i % 2 == 0:
                even.append(parts[i])
        print(" ".join(even))
    elif command[0] == "Check" and command[1] == "Odd":
        odd = []
        for i in range(len(parts)):
            if i % 2 == 1:
                odd.append(parts[i])
        print(" ".join(odd))
    command = input().split()
else:
    print(f"You crafted {''.join(parts)}!")
