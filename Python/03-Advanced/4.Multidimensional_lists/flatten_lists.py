text = input().split("|")
matrix = [x.split() for x in text]
print(' '.join([' '.join(x) for x in matrix[::-1] if x]))