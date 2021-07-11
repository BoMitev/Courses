import sys
n = int(input())
minimum_odd = sys.maxsize
maximum_odd = -sys.maxsize
minimum_even = sys.maxsize
maximum_even = -sys.maxsize
sum_odd = 0
sum_even = 0

for number in range(1, n+1):
    value = float(input())
    if number % 2 == 1:
        if value > maximum_odd:
            maximum_odd = value
        if value < minimum_odd:
            minimum_odd = value
        sum_odd += value
    else:
        if value > maximum_even:
            maximum_even = value
        if value < minimum_even:
            minimum_even = value
        sum_even += value

print(f"OddSum={sum_odd:.2f},")
if minimum_odd == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={minimum_odd:.2f},")
if maximum_odd == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={maximum_odd:.2f},")

print(f"EvenSum={sum_even:.2f},")
if minimum_even == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={minimum_even:.2f},")
if maximum_even == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={maximum_even:.2f}")