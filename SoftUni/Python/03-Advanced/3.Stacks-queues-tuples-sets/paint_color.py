from collections import deque

data = deque(input().split())
main = ["red", "yellow", "blue", "orange", "purple", "green"]
stack = []

while data:
    first = data.popleft()
    second = ""
    if data:
        second = data.pop()

    if second+first in main:
        sub = second+first
    else:
        sub = first+second

    if sub in main:
        stack.append(sub)
    else:
        data = list(data)
        count = len(data) // 2
        first_half = data[:count]
        second_half = data[count:]
        first_half.append(first[:-1])
        first_half.append(second[:-1])
        data = deque(filter(len, first_half + second_half))

for color in stack:
    if color == "orange":
        if "red" and "yellow" not in stack:
            stack.remove(color)
    elif color == "purple":
        if "red" and "blue" not in stack:
            stack.remove(color)
    elif color == "green":
        if "yellow" and "blue" not in stack:
            stack.remove(color)
print(stack)
