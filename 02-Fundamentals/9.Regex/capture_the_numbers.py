import re
lines = []
while True:
    txt = input()
    if txt:
        lines.append(txt)
    else:
        break
nums = []
for line in lines:
    res = re.findall(r"\d+", line)
    for r in res:
        nums.append(r)
print(' '.join(nums))