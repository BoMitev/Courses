password = input()

while True:
    command = input().split()
    if command[0] == "Done":
        break
    if command[0] == "TakeOdd":
        new_password = ""
        for char in range(len(password)):
            if char % 2 == 1:
                new_password += password[char]
        password = new_password
        print(password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring = password[index:index+length]
        password = password.replace(substring, "", 1)
        print(password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")