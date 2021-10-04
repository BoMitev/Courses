text = input().split(">")
strength = 0

for i in range(1, len(text)):
    item = text[i]
    if len(item) == int(item[0]):
        text[i] = " "
    elif len(item) < int(item[0]):
        strength += (int(item[0]) - len(item))
        text[i] = " "
    elif len(item) > int(item[0]):
        strength += int(item[0])
        text[i] = item[strength:]
        strength -= int(item[0])

text = ">".join(text)
format = text.replace(" ", "")
print(format)