def type_check(check):
    def decorator(func):
        def wrapper(param):
            if isinstance(param, check):
                return func(param)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
