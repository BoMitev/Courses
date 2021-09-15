# num = list(input())
# num.sort(reverse=True)
#
# for k in range(len(num)):
#     print(num[k], end="")

num = input()
number = ""

while True:
    number += max(num)
    num = num.replace(max(num), '', 1)
    if num == "":
        break
print(int(number))