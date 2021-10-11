def print_triangle(size):
    list = []
    for row in range(1, size + 1):
        list.append(row)
        print(*list)

    for row in range(size - 1, 0, -1):
        list.pop()
        print(*list)