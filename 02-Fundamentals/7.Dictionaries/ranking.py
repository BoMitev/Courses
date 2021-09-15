passwords = {}
contests = {}

command = input()
while command != "end of contests":
    contest, password = command.split(":")
    if contest not in passwords:
        passwords[contest] = ""
    passwords[contest] = password
    command = input()

data = input()
while data != "end of submissions":
    cont, user_password, user, points = data.split("=>")
    if cont in passwords:
        if passwords[cont] == user_password:
            if user not in contests:
                contests[user] = {cont: int(points)}
            else:
                if cont in contests[user].keys():
                    if contests[user][cont] < int(points):
                        contests[user][cont] = int(points)
                else:
                    contests[user][cont] = int(points)
    data = input()

winner = ["", 0]
for key,value in contests.items():
    if winner[1] < sum(value.values()):
        winner[0] = key
        winner[1] = sum(value.values())

print(f"Best candidate is {winner[0]} with total {winner[1]} points.\nRanking:")
for k,v in sorted(contests.items(), key=lambda x: x[0]):
    print(k)
    for key,value in sorted(v.items(), key=lambda x: -x[1]):
        print(f"#  {key} -> {value}")
