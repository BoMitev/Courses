n = int(input())
odd = set()
even = set()

for row in range(n):
    name = input()
    total = 0
    for char in name:
        total += ord(char)
    total /= row+1
    if int(total) % 2 == 0:
        even.add(int(total))
    elif int(total) % 2 == 1:
        odd.add(int(total))

if sum(odd) == sum(even):
    union = odd.update(even)
    odd = [str(x) for x in odd]
    print(', '.join(odd))
elif sum(odd) > sum(even):
    difference = even.difference_update(odd)
    odd = [str(x) for x in odd]
    print(', '.join(odd))
elif sum(odd) < sum(even):
    symetric = odd.symmetric_difference_update(even)
    odd = [str(x) for x in odd]
    print(', '.join(odd))