import sys

n = int(input())
max = -sys.maxsize
sum = 0

for number in range(1, n+1):
    value = int(input())
    if value > max:
        max = value
    sum += value

sum_others = sum - max
if max == sum_others:
    print("Yes")
    print(f"Sum = {max}")
else:
    print("No")
    print(f"Diff = {abs(max - sum_others)}")
