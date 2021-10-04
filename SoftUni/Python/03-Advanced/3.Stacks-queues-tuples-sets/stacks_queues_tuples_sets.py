first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "Check" and command[1] == "Subset":
        print(first.issuperset(second))
        continue
    for x in command[2::1]:
        if command[0] == "Add":
            if command[1] == "First":
                first.add(int(x))
            else:
                second.add(int(x))
        elif command[0] == "Remove":
            if command[1] == "First":
                first.discard(int(x))
            elif command[1] == "Second":
                second.discard(int(x))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")