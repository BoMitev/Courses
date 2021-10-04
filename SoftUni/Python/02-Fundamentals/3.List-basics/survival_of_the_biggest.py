nums = input().split()
n = int(input())

for i in range(len(nums)):
    nums[i] = int(nums[i])

for x in range(n):
    nums.remove(min(nums))

for i in range(len(nums)):
    nums[i] = str(nums[i])

print(", ".join(nums))