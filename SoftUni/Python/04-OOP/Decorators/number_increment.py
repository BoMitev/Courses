def number_increment(nums):
    def increase():
        return [x+1 for x in nums]

    return increase()


print(number_increment([1, 2, 3]))