tab = int(input())
salary = int(input())

for number in range(1, tab+1):
    value = input()
    if value == "Facebook":
        salary -= 150
    elif value == "Instagram":
        salary -= 100
    elif value == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break
if salary > 0:
    print(salary)