def factoriel_first(num_1):
    factoriel = num_1
    for x in range(1, num_1):
        factoriel *= (num_1 - x)
    return factoriel

def factoriel_second(num_2):
    factoriel = num_2
    for x in range(1, num_2):
        factoriel *= (num_2 - x)
    return factoriel

def division(num_1, num_2):
    result = factoriel_first(num_1) /  factoriel_second(num_2)
    print(f"{result:.2f}")
first_num = int(input())
second_num = int(input())

division(first_num, second_num)