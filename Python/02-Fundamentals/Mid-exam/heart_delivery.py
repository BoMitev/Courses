neighborhood = [int(x) for x in input().split("@")]
command = input()
last_position = 0

while command != "Love!":
    command = command.split()
    length = int(command[1])
    last_position += length
    if command[0] == "Jump":
        if last_position > len(neighborhood)-1:
            last_position = 0
        if neighborhood[last_position] - 2 == 0:
            neighborhood[last_position] -= 2
            print(f"Place {last_position} has Valentine's day.")
        elif neighborhood[last_position] == 0:
            print(f"Place {last_position} already had Valentine's day.")
        else:
            neighborhood[last_position] -= 2
    command = input()
print(f"Cupid's last position was {last_position}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    count = [x for x in neighborhood if x > 0]
    print(f"Cupid has failed {len(count)} places.")
