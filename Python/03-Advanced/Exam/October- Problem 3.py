# Write function called best_list_pureness which will receive a list of numbers and a number K. You have to rotate the list
# K times (last becomes first) to find the variation of the list with the best pureness (pureness is calculated by summing
# all the elements in the list multiplied by their indices). For example, in the list [4, 3, 2, 6] with the best pureness
# is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26. At the end the function should return a string containing the highest pureness
# and the amount of rotations that were made to find this pureness in the following format: "Best pureness {pureness_value}
# after {count_rotations} rotations". If there is more than one highest pureness, take the first one.

def best_list_pureness(nums, k, pureness=float('-inf'), best_rotation=0, current_rotation=0):
    if k+1 == 0:
        return f"Best pureness {pureness} after {best_rotation} rotations"

    total = 0
    for i in range(len(nums)):
        total += (i * nums[i])
    if total > pureness:
        pureness = total
        best_rotation = current_rotation

    nums = nums[-1:]+nums[:-1]
    return best_list_pureness(nums, k-1, pureness=pureness, best_rotation=best_rotation, current_rotation=current_rotation+1)



test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
