import re
num = int(input())

for i in range(num):
    sequence = input()
    name = re.search(r"(?<=@)\w+(?=\|)", sequence)
    age = re.search(r"(?<=#)\d+(?=\*)", sequence)
    if name and age:
        print(f"{name.group()} is {age.group()} years old.")
