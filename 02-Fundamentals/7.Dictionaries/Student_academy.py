n = int(input())
academy = {}

for i in range(n):
    name = input()
    grade = float(input())
    if name not in academy:
        academy[name] = []
    academy[name].append(grade)

for k,v in sorted(academy.items(), key=lambda x: -(sum(x[1])/len(x[1]))):
    if sum(v)/len(v) >= 4.5:
        print(f"{k} -> {sum(v)/len(v):.2f}")