import math
income = float(input())
average_success = float(input())
minimal_salary = float(input())

social_scholarship = math.floor(minimal_salary * 0.35)
success_scholarship = math.floor(average_success * 25)

if average_success >= 5.5 and income < minimal_salary and social_scholarship >= success_scholarship:
    print(f"You get a Social scholarship {social_scholarship} BGN")
elif average_success >= 5.5 and income < minimal_salary and social_scholarship < success_scholarship:
    print(f"You get a scholarship for excellent results {success_scholarship} BGN")
elif average_success > 4.5 and income < minimal_salary:
    print(f"You get a Social scholarship {social_scholarship} BGN")
elif average_success >= 5.5:
    print(f"You get a scholarship for excellent results {success_scholarship} BGN")
else:
    print("You cannot get a scholarship!")