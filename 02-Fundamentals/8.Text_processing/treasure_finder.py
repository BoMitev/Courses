import re
keys = [int(x) for x in input().split()]

command = input()
while command != "find":
    message = ""
    index = 0
    for i in range(len(command)):
        if index == len(keys):
            index = 0
        message += chr(ord(command[i]) - keys[index])
        index += 1
    treasure = re.search(r"(?<=&)\w+(?=&)", message)
    place = re.search(r"(?<=\<)\w+(?=\>)", message)
    print(f"Found {treasure.group()} at {place.group()}")
    command = input()