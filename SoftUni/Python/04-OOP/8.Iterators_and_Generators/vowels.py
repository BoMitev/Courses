class vowels:
    _VOWELS = "AEIOUaeiou"

    def __init__(self, iterable):
        self.iterable = [char for char in iterable if char in self._VOWELS]
        self.index = 0
        self.end = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.end:
            raise StopIteration

        value = self.iterable[self.index]
        self.index += 1
        return value


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
