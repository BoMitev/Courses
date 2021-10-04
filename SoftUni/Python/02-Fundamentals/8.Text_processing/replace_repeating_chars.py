text = input()
new = text[0]

for char in text:
    if new[-1] != char:
        new += char

print(new)