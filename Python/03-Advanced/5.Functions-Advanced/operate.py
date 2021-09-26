from functools import reduce


def operate(operator, *nums):
    return reduce(lambda a, b: eval(f"{a} {operator} {b}"), nums)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))