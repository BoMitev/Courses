stops = input()
command = input().split(":")

while command[0] != "Travel":
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
    elif command[0] == "Remove Stop":
        index = int(command[1])
        end = int(command[2])
        if 0 <= end < len(stops):
            stops = stops[:index] + stops[end+1:]
    elif command[0] == "Switch":
        old = command[1]
        new = command[2]
        stops = stops.replace(old, new)
    print(stops)
    command = input().split(":")
else:
    print(f"Ready for world tour! Planned stops: {stops}")
