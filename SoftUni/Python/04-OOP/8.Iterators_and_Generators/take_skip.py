class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration

        value = self.num
        self.num += self.step
        self.count -= 1
        return value


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

