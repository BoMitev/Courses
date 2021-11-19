from itertools import permutations

def possible_permutations(nums):
    permutations_data = permutations(nums, len(nums))
    for el in permutations_data:
        yield list(el)

[print(n) for n in possible_permutations([1, 2, 3])]