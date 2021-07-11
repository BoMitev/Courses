string_1 = input().split(", ")
string_2 = input().split(", ")

list = []
for word in string_1:
    for string in string_2:
        x = string.count(word)
        if x > 0 and word not in list:
            list.append(word)

print(list)