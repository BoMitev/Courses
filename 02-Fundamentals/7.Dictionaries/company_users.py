company_users = {}
command = input()

while command != "End":
    company, id = command.split(" -> ")
    if company not in company_users:
        company_users[company] = []
    if id not in company_users[company]:
        company_users[company].append(id)
    command = input()


for k,v in sorted(company_users.items(), key=lambda x: x[0]):
    print(k)
    for i in v:
        print(f"-- {i}")