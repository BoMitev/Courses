# Write a function called numbers_searching which receives a different amount of parameters. All parameters will be integer numbers forming a sequence of consecutive numbers. Your task is to find an unknown amount of duplicates from the given sequence and a missing value, such that all the duplicate values and the missing value are between the smallest and the biggest received number.
# The function should return a list with the last missing number as a first argument and a sorted list, containing the duplicates found, in ascending order.
# For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as duplicate numbers in the following format: [3, [2, 4]]



# First solving
def numbers_searching(*args, missing_n=None, res=None):
    if not args:
        res.sort()
        return [missing_n, res]

    if res is None:
        high, low, res = max(args), min(args), []
        missing_numbers = [n for n in range(low, high) if n not in args]
        if missing_numbers:
            missing_n = missing_numbers[-1]

    if args.count(args[0]) > 1 and args[0] not in res:
        res.append(args[0])

    return numbers_searching(*args[1:], missing_n=missing_n, res=res)

# Second solving
# def numbers_searching(*nums):
#     dublicated = sorted(list(set([x for x in nums if nums.count(x) > 1])))
#     missing_num = sorted(set(range(min(nums), max(nums))).difference(nums))
#     return [missing_num[-1], dublicated]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
print(numbers_searching(1, 2, 4, 2, 6, 4, 6))
