def even_odd(*nums):
    if nums[-1] == "odd":
        result = list(filter(lambda x: x % 2 != 0, nums[:-1]))
    else:
        result = list(filter(lambda x: x % 2 == 0, nums[:-1]))
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))