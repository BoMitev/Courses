def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                return False
        else:
            return True

    return False

def get_primes(args):
    for el in args:
        if is_prime(el):
            yield el



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))