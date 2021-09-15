from collections import deque

operators = ["*", "+", "-", "/"]
expression = input().split()
stack = deque()

for item in expression:
    if item not in operators:
        stack.append(int(item))
    else:
        while len(stack) > 1:
            first = stack.popleft()
            second = stack.popleft()
            if item == "*":
                stack.appendleft(int(first*second))
            elif item == "+":
                stack.appendleft(int(first+second))
            elif item == "-":
                stack.appendleft(int(first-second))
            elif item == "/":
                stack.appendleft(int(first/second))
print(stack[0])
