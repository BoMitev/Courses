text = input()
count = {}
for char in text:
    if char != " ":
        if char not in count:
            count[char] = 0
        count[char] += 1

for k,v in count.items():
    print(f"{k} -> {v}")