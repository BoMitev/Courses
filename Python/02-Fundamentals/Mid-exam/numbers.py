numbers = [int(x) for x in input().split()]

average = sum(numbers) / len(numbers)
top_5 = [x for x in numbers if x > average]

if len(top_5) < 1:
    print("No")
else:
    top_5.sort(reverse=True)
    top_5 = [str(x) for x in top_5]
    print(" ".join(top_5[:5]))