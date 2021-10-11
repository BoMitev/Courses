def operation(num1, sign, num2):
    number_1 = float(num1)
    number_2 = int(num2)
    if sign == "/":
        return number_1 / number_2
    elif sign == "*":
        return number_1 * number_2
    elif sign == "-":
        return number_1 - number_2
    elif sign == "+":
        return number_1 + number_2
    elif sign == "^":
        return number_1 ** number_2
