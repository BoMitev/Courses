import re
txt = input()
total_pairs = 0
mirrors = []
pattern = r"(\@|\#)(?P<name1>[A-Za-z]{3,})(\1)(\1)(?P<name2>[A-Za-z]{3,})(\1)"
results = re.finditer(pattern, txt)

for result in results:
    name1 = result.group('name1')
    name2 = result.group('name2')
    if name1 == name2[::-1]:
        mirrors.append(f"{name1} <=> {name2}")
    total_pairs += 1

if total_pairs < 1:
    print("No word pairs found!")
else:
    print(f"{total_pairs} word pairs found!")

if len(mirrors) < 1:
    print("No mirror words!")
else:
    print(f"The mirror words are:\n{', '.join(mirrors)}")
