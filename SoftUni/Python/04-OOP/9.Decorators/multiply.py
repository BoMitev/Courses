import functools


def multiply(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            result = func(*args)
            return result * times

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
