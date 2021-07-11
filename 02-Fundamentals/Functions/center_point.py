import math


def measure(num_1, num_2):
    x = (0 - abs(num_1))**2 + (0 - abs(num_2))**2
    return x


def closest(num_1, num_2, num_3, num_4):
    if measure(num_1, num_2) <= measure(num_3, num_4):
        print(f"({math.floor(num_1)}, {math.floor(num_2)})")
    else:
        print(f"({math.floor(num_3)}, {math.floor(num_4)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

closest(x1, y1, x2, y2)
