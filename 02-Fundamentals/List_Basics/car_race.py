nums = input().split()

finish = len(nums) // 2
left_side = nums[0:finish]
right_side = nums[:finish:-1]
left_time = 0
right_time = 0
for x in left_side:
    if int(x) == 0:
        left_time *= 0.8
    else:
        left_time += int(x)

for k in right_side:
    if int(k) == 0:
        right_time *= 0.8
    else:
        right_time += int(k)

if right_time > left_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")