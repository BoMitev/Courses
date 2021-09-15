import re

text = input()
items = []
pattern = r"(#|\|)(?P<item>[A-Za-z\s]+)(\1)(?P<date>\d{2}\/\d{2}\/\d{2})(\1)(?P<calories>\d+)(\1)"
results = re.finditer(pattern, text)
total = 0
for result in results:
    items.append(f"{result.group('item')}#{result.group('date')}#{result.group('calories')}")
    total += int(result.group('calories'))

print(f"You have food to last you for: {total // 2000} days!")
for i in items:
    item, date, calories = i.split("#")
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")