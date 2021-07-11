string = list(input())
upper = []

for i in range(len(string)):
    if string[i].isupper():
        upper.append(i)
print(upper)