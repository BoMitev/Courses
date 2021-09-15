statistic = {}
individual = {}
command = input()

while command != "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)
    if contest not in statistic:
        statistic[contest] = {}
    if username not in statistic[contest]:
        statistic[contest][username] = 0
    if statistic[contest][username] < points:
        statistic[contest][username] = points
    command = input()

for k,v in statistic.items():
    print(f"{k}: {len(v.values())} participants")
    count = 1
    for user, point in sorted(v.items(), key= lambda x: (-x[1],x[0])):
        print(f"{count}. {user} <::> {point}")
        count +=1
        if user not in individual:
            individual[user] = 0
        individual[user] += point

track = 1
print("Individual standings:")
for k, v in sorted(individual.items(), key= lambda x: (-x[1],x[0])):
    print(f"{track}. {k} -> {v}")
    track += 1
