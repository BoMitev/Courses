import math

def calculate_log(x, base_as_str):
    if base_as_str == "natural":
        return math.log(x)

    base = int(base_as_str)
    return math.log(x, base)


print(calculate_log(10, 10))
print(calculate_log(1024, 2))
