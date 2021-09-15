year = int(input())

while True:
    year += 1
    str_year = str(year)
    happy_year = True
    for i in range(len(str_year)):
        digit = str_year[i]
        for j in range(len(str_year)):
            if digit == str_year[j] and not i == j:
                happy_year = False
                break
    if happy_year:
        print(str_year)
        break

#    if len(str_year) == len(set(str_year)):
#        print(year)
#        break