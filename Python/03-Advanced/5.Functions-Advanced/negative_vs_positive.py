def positive_nums(nums):
    positive = list(filter(lambda nums: nums > 0, nums))
    return sum(positive)

def negative_nums(nums):
    negative = list(filter(lambda nums: nums < 0, nums))
    return sum(negative)

def compare(nums):
    print(negative_nums(nums))
    print(positive_nums(nums))
    if abs(negative_nums(nums)) > positive_nums(nums):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nums = [int(x) for x in input().split()]
compare(nums)