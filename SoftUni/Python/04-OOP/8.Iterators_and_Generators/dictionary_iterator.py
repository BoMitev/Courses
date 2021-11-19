class dictionary_iter:
    def __init__(self, kwargs: dict):
        self.kwargs = kwargs
        self.items = tuple(self.kwargs.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.items):
            raise StopIteration

        value = self.items[self.index]
        self.index += 1
        return value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
