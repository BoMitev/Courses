first_number_ceil = int(input())
second_number_ceil = int(input())
third_number_ceil = int(input())

for first in range(1, first_number_ceil + 1):
    for second in range(1, second_number_ceil + 1):
        for third in range(1, third_number_ceil + 1):
            prime = True
            for i in range(2, second):
                if (second % i) == 0:
                    prime = False
            if first % 2 == 0 and third % 2 == 0 and 1 < second < 8 and prime:
                print(first, second, third)