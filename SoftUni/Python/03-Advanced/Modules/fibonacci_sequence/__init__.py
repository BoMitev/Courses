numbers = [0, 1]



def create_sequence(n):
    global numbers
    numbers = [0, 1]
    for i in range(2, n):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return ' '.join(str(x) for x in numbers)


def locate(x):
    if x not in numbers:
        raise IndexError(f'Number {x} not in the sequence')

    return f'The number - {x} is at index {numbers.index(x)}'