import math
persons = int(input())
capacity = int(input())

courses = persons / capacity
print(math.ceil(courses))