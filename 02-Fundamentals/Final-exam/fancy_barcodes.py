import re
n = int(input())
barcode_pattern = r"(@{1}\#+)(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])(@{1}\#+)"

for _ in range(n):
    txt = input()
    results = re.finditer(barcode_pattern, txt)
    if re.search(barcode_pattern, txt) is not None:
        for result in results:
            barcode = result.group("barcode")
            if re.search(r"\d+", barcode) is None:
                print("Product group: 00")
            else:
                group = re.findall(r"\d+", barcode)
                print(f"Product group: {''.join(group)}")
    else:
        print("Invalid barcode")