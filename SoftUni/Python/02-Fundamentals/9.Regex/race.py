import re
dict = {}
players = input().split(", ")
for player in players:
    dict[player] = 0

command = input()
while command != "end of race":
    name = "".join(re.findall(r"([A-Za-z])", command))
    result = re.findall(r"\d", command)
    total = sum([int(x) for x in result])
    if name in dict:
        dict[name] += total
    command = input()

dict = sorted(dict.items(), key=lambda x: -x[1])
print(f"1st place: {dict[0][0]}")
print(f"2nd place: {dict[1][0]}")
print(f"3rd place: {dict[2][0]}")
