clothes = [int(x) for x in input().split()]
capacity = int(input())
number_of_boxes = 0

temp = 0
while clothes:
    cloth = clothes.pop()
    if temp+cloth <= capacity:
        temp += cloth
    else:
        number_of_boxes += 1
        temp = 0
        clothes.append(cloth)

if temp > 0:
    number_of_boxes += 1

print(number_of_boxes)