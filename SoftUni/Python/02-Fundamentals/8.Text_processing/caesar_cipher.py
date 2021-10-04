text = input()

for char in text:
    char = chr(ord(char)+3)
    print(char, end="")