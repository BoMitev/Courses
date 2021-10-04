def math_operations(*args, i=0, **diction):
    args = list(args)
    if len(args) == 0:
        return diction

    values = ["a", "s", "d", "m"]
    if values[i] == "a":
        diction[values[i]] += args[0]
    elif values[i] == "s":
        diction[values[i]] -= args[0]
    elif values[i] == "d":
        try:
            diction[values[i]] /= args[0]
        except ZeroDivisionError:
            pass
    elif values[i] == "m":
        diction[values[i]] *= args[0]
        i = -1
    return math_operations(*args[1:], i = i+1, **diction)


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))