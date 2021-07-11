nums = input().split(", ")

for x in nums:
    if x == "0":
        nums.append(x)
        nums.remove(x)
nums = [int(x) for x in nums]
print(nums)