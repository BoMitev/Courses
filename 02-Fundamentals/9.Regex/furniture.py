import re
total_cost = 0
furniture = []
pattern = r"(\s|\A)(>>){1}(?P<item>\w+)<<(?P<price>\d+([.]\d+)*)!(?P<count>\d+)"
command = input()
while command != "Purchase":
    results = re.finditer(pattern, command)
    for result in results:
        price = float(result.group("price")) * int(result.group("count"))
        item = result.group("item")
        total_cost += price
        furniture.append(item)
    command = input()

print("Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")