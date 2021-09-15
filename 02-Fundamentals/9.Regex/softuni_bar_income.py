import re
command = input()
total = 0
pattern = r"\%(?P<name>[A-Z][a-z]+)%[^\|\$\%\.]*<(?P<item>\w+)>[^\|\$\%\.]*\|(?P<count>\d+)\|[^\|\$\%\.]*?(?P<price>[-+]?[0-9]*\.?[0-9]+)\$"
while command != "end of shift":
    results = re.finditer(pattern, command)
    for result in results:
        current = int(result.group("count")) * float(result.group("price"))
        print(f"{result.group('name')}: {result.group('item')} - {current:.2f}")
        total += current
    command = input()
else:
    print(f"Total income: {total:.2f}")