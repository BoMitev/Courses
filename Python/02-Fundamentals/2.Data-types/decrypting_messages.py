key = int(input())
n = int(input())
message = ""

for i in range(n):
    letter = input()
    encrypt = ord(letter) + key
    message += chr(encrypt)

print(message)
