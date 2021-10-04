def func_executor(*args, result=[]):
    if not args:
        return result

    function, arguments = args[0][0], args[0][1]
    result.append(function(*arguments))
    return func_executor(*args[1:], result=result)


# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
