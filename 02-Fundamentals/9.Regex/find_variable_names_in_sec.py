import re
txt = input()
result = re.findall(r"(?<=\b_)[A-Za-z0-9]+\b", txt)
print(",".join(result))