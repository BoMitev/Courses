import re
text = input()
destinations = []
distance = 0
pattern = r"(\=|\/)(?P<desti>[A-Z][A-Za-z]{2,})\1"
results = re.finditer(pattern, text)

for result in results:
    destinations.append(result.group('desti'))
    distance += len(result.group('desti'))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {distance}")