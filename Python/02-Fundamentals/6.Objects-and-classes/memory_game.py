elements = input().split()
command = input().split()
moves = 0

while command[0] != "end":
    if len(elements) < 1:
        break
    index_1 = int(command[0])
    index_2 = int(command[1])
    moves += 1
    if index_1 != index_2 and 0 <= index_1 < len(elements) and 0 <= index_2 < len(elements):
        if elements[index_1] == elements[index_2]:
            print(f"Congrats! You have found matching elements - {elements[index_1]}!")
            if index_1 > index_2:
                elements.pop(index_1)
                elements.pop(index_2)
            else:
                elements.pop(index_2)
                elements.pop(index_1)
        else:
            print("Try again!")
    else:
        elements.insert(len(elements) // 2, f"-{moves}a")
        elements.insert(len(elements) // 2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    command = input().split()

if len(elements) > 0:
    print("Sorry you lose :(\n" + " ".join(elements))
else:
    print(f"You have won in {moves} turns!")