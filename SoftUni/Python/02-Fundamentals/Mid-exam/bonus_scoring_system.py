students = int(input())
lectures = int(input())
bonus = int(input())
max = 0
att = 0

for _ in range(students):
    attendance = int(input())
    total = attendance/lectures * (5 + bonus)
    if total > max:
        max = total
        att = attendance

print(f"Max Bonus: {round(max)}.")
print(f"The student has attended {att} lectures.")
