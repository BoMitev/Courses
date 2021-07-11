string = input()
list = string.split(", ")
counter = 0
position = 0

if list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(list)):
        if list[i] == "sheep":
            counter += 1
        else:
            counter = 0
    print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
