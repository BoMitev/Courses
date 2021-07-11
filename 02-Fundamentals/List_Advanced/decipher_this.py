import re
message = input().split()
for word in message:
    res = re.split('(\d+)', word)
    split = res[2]
    if len(split) > 1:
        print(chr(int(res[1])), end="")
        print(split[-1], end="")
        print(split[1:-1], end="")
        print(split[0], end=" ")
    else:
        print(chr(int(res[1])), end="")
        print(split[-1], end="")
        print(split[1:-1], end=" ")