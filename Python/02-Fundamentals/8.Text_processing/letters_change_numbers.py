text = input().split()
total = 0

for sub in text:
    before = sub[0]
    number = int(sub[1:-1])
    after = sub[-1]
    if before.isupper():
        number /= (ord(before)-64)
    elif before.islower():
        number *= (ord(before)-96)
    if after.isupper():
        number -= (ord(after)-64)
    elif after.islower():
        number += (ord(after)-96)
    total += number

print(f"{total:.2f}")