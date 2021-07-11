figure = input()

if figure == "square":
    side = float(input())
    print(f'{round(side * side, 3)}')
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    print(f'{round(side_a * side_b, 3)}')
elif figure == "circle":
    import math
    radius = float(input())
    print(f"{round(math.pi * radius * radius, 3)}")
elif figure == "triangle":
    side = float(input())
    height = float(input())
    print(f"{round(side * height / 2, 3)}")