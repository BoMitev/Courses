number_of_groups = int(input())
musala = 0
monblan = 0
kiliman = 0
k2 = 0
everest = 0
total = 0

for group in range(0, number_of_groups):
    number_of_persons = int(input())
    if number_of_persons <= 5:
        musala += number_of_persons
    elif number_of_persons <= 12:
        monblan += number_of_persons
    elif number_of_persons <= 25:
        kiliman += number_of_persons
    elif number_of_persons <= 40:
        k2 += number_of_persons
    else:
        everest += number_of_persons
    total += number_of_persons

print(f"{musala/total*100:.2f}%")
print(f"{monblan/total*100:.2f}%")
print(f"{kiliman/total*100:.2f}%")
print(f"{k2/total*100:.2f}%")
print(f"{everest/total*100:.2f}%")
