age = float(input())
sex = input()

if sex == "m" and age >= 16:
    print("Mr.")
elif sex == "m" and age < 16:
    print("Master")
elif sex == "f" and age >= 16:
    print("Ms.")
elif sex == "f" and age < 16:
    print("Miss")