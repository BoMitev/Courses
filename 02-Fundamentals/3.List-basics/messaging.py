code = input().split()
string = input()
string = [x for x in string]
message = []
for symbol in code:
    char = [int(x) for x in symbol]
    if len(string) < sum(char)+1:
        index = sum(char) - len(string)
    else:
        index = sum(char)
    message.append(string[index])
    string.pop(index)
print("".join(message))