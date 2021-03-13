number_1 = int(input('Enter your first number: '))
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
number_2 = int(input('Enter your second number: '))

print(f'{number_1} {operation} {number_2} = ', end='')
if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    print(number_1 / number_2)
else:
    print('Math operation not supported')