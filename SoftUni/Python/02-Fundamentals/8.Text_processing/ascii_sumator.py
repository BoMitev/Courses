first_char = ord(input())
second_char = ord(input())
text = input()
total = 0

for char in text:
    if first_char < ord(char) < second_char:
        total += ord(char)
print(total)