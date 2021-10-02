class VariableMustBeIntegerError(Exception):
    def __init__(self):
        super().__init__('Variable times must be ant integer')


text = input()
times = input()

if not times.isdigit():
    raise VariableMustBeIntegerError()
print(text * int(times))
