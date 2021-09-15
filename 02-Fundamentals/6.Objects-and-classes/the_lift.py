people = int(input())
lift = [int(x) for x in input().split()]
wagon_space = 4

for i in range(len(lift)):
    if lift[i] < wagon_space:
        available_space = wagon_space - lift[i]
        if people - available_space >= 0:
            lift[i] += available_space
            people -= available_space
        else:
            lift[i] += people
            people -= people

lift_space = wagon_space * len(lift)
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif lift_space > sum(lift):
    print("The lift has empty spots!")

lift = [str(x) for x in lift]
print(" ".join(lift))