chars = int(input())
sum = 0

for _ in range(chars):
    value = input()
    sum += ord(value)
print(f"The sum equals: {sum}")