string1, string2 = input().split()
total = 0

shorter_string = min(len(string1), len(string2))

for i in range(shorter_string):
    char_string1 = string1[i]
    char_string2 = string2[i]
    total += (ord(char_string1) * ord(char_string2))

longer_string = max(len(string1), len(string2))
for x in range(shorter_string, longer_string):
    if len(string1) > len(string2):
        total += ord(string1[x])
    else:
        total += ord(string2[x])

print(total)