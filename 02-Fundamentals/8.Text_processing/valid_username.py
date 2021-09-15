import re
usernames = input().split(", ")

for user in usernames:
    check = bool(re.match("^[A-Za-z0-9_-]*$", user))
    if 3 <= len(user) <= 16 and check:
        print(user)
