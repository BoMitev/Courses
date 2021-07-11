import math
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
student_count = int(input())

students_per_hour = first_employee + second_employee + third_employee
hours = 0
while student_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    student_count -= students_per_hour

print(f"Time needed: {hours}h.")