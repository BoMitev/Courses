def check(data):
    stack = []
    for i in data:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

data = input()
print(check(data))
