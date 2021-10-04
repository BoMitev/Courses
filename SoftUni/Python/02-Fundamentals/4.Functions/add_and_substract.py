def sum_numbers(num_1: int, num_2: int):
    return num_1 + num_2


def subtract(sum_1: int, num_3: int):
    return sum_1 - num_3


def add_and_substract(num_1: int, num_2: int, num_3: int):
    sum_1 = sum_numbers(num_1, num_2)
    result = subtract(sum_1, num_3)
    return result


a = int(input())
b = int(input())
c = int(input())

print(add_and_substract(a, b, c))