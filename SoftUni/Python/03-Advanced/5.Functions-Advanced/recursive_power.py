def recursive_power(num, power, result=1, index=0):
    if index == power:
        return result

    result *= num
    return recursive_power(num, power, result, index+1)




print(recursive_power(10, 100))