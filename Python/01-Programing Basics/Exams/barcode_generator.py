start = int(input())
end = int(input())

for number in range(start, end):
        first_start = int(number / 1000)
        second_start = int((number / 100) % 10)
        third_start = int((number / 10) % 10)
        fourth_start = int(number % 10)
        if first_start % 2 != 0 and second_start % 2 != 0 and third_start % 2 != 0 and fourth_start % 2 != 0:
                print(number, end=' ')