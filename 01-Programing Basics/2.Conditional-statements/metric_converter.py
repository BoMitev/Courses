size = float(input())
unit = input()
convert_unit = input()

if unit == "mm":
    size /= 1000
elif unit == "cm":
    size /= 100

if convert_unit == "mm":
    size *= 1000
elif convert_unit == "cm":
    size *= 100

print(f"{size:.3f}")
