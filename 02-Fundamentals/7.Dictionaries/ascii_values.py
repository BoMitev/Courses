char = input().split(", ")
codes = {char[i]: ord(char[i]) for i in range(len(char))}
print(codes)