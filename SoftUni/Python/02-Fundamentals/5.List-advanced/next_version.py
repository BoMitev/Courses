current_version = input().split(".")
int_next_version = int("".join(current_version))+1
next_version = []
for num in str(int_next_version)[-1::-1]:
    next_version.insert(0, num)
print(".".join(next_version))