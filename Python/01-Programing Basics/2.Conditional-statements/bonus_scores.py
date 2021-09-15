number = int(input())

if number <= 100:
    bonus = 5
elif 100 < number < 1000:
    bonus = number * 0.2
else:
    bonus = number * 0.1

if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2
print(bonus)
print(number + bonus)