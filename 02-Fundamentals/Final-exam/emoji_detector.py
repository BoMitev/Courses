import re
txt = input()
emoji_pattern = r"(?P<emoji>(::|\*\*)[A-Z][a-z]{2,}(\2))"
find_nums = re.findall(r"\d", txt)
threshold = 1
for i in find_nums:
    threshold *= int(i)
print(f"Cool threshold: {threshold}")

total_emojis = 0
list_of_cool_emojis = []
results = re.finditer(emoji_pattern, txt)
for result in results:
    emoji = result.group('emoji')
    total_emojis += 1
    cool_count = 0
    for char in emoji[2:-2]:
        cool_count += ord(char)
    if cool_count >= threshold:
        list_of_cool_emojis.append(emoji)
print(f"{total_emojis} emojis found in the text. The cool ones are:")

if len(list_of_cool_emojis) > 0:
    print('\n'.join(list_of_cool_emojis))