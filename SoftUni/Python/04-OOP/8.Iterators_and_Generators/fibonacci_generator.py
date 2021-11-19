def fibonacci():
    current = 0
    prev = 1
    while True:
        yield current
        current = prev + current
        prev = current - prev


generator = fibonacci()
for i in range(5):
    print(next(generator))
