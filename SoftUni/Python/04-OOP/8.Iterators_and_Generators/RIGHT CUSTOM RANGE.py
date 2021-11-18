class custom_range_iterator:
    def __init__(self, custom_range):
        self.custom_range = custom_range
        self.current_number = self.custom_range.start

    def __next__(self):
        if self.current_number > self.custom_range.end:
            raise StopIteration

        value = self.current_number
        self.current_number += 1

        return value


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return custom_range_iterator(self)


