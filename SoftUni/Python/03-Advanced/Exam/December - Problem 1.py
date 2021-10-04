# First you will be given a sequence of integers representing males. Afterwards you will be given another sequence of
# integers representing females.

# You have to start from the first female and try to match it with the last male.
#   If their values are equal, you have to match them and remove both of them. Otherwise you should remove only the
#   female and decrease the value of the male by 2.
#   If someone’s value is equal to or below 0, you should remove him/her from the records before trying to match him/her
#   with anybody.
#   Special case - if someone’s value divisible by 25 without remainder, you should remove him/her and the next person
#   of the same gender.

# You need to stop matching people when you have no more females or males.

from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
count = 0

while males and females:
    if females[0] <= 0 or males[-1] <= 0:
        if females[0] <= 0:
            females.popleft()
        if males[-1] <= 0:
            males.pop()
        continue

    if females[0] % 25 == 0 or males[-1] % 25 == 0:
        if females[0] % 25 == 0:
            females.popleft()
            females.popleft()
        if males[-1] % 25 == 0:
            males.pop()
            males.pop()
        continue

    female, male = females.popleft(), males.pop()
    if female == male:
        count += 1
    else:
        males.append(male - 2)

print(f"Matches: {count}")
if males:
    print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")
