divisor = int(input())
bound = int(input())
num = True
while num:
    if bound % divisor != 0:
        bound -= 1
    else:
        print(bound)
        num = False
