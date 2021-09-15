numbers = [int(x) for x in input().split()]
command = input().split()

while command[0] != "end":
    if command[0] == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]
    elif command[0] == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        numbers[index_1] *= numbers[index_2]
    elif command[0] == "decrease":
        numbers = [x-1 for x in numbers]
    command = input().split()
numbers = [str(x) for x in numbers]
print(", ".join(numbers))