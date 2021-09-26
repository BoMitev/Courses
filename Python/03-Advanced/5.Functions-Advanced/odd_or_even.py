def odd_or_even(command, nums):
    if command == "Odd":
        result = list(filter(lambda x: x % 2 != 0, nums))
    else:
        result = list(filter(lambda x: x % 2 == 0, nums))
    return result


command = input()
nums = [int(x) for x in input().split()]
print(sum(odd_or_even(command, nums)) * len(nums))