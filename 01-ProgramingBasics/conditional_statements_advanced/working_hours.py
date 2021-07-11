time = int(input())
day = input()

if 10 <= time <= 18:
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
        print("open")
    else:
        print("closed")
else:
    print("closed")