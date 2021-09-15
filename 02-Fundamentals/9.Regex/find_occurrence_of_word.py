import re
text = input().lower()
word = input().lower()
result = re.findall(rf"\b{word}\b", text)
print(len(result))