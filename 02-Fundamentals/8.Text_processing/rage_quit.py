import re
text = input().upper()
text_list = (re.findall('\d+|\D+',text))
unique = [text_list[x] for x in range(len(text_list)) if x % 2 != 1]
unique = len(set(''.join(unique)))

print(f"Unique symbols used: {unique}")
for i in range(len(text_list)):
    if i % 2 != 1:
        print(text_list[i] * int(text_list[i+1]), end="")