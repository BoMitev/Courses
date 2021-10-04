secret_message = input()
command = input().split(":|:")

while command[0] != "Reveal":
    if command[0] == "InsertSpace":
        i = int(command[1])
        secret_message = secret_message[:i] + ' ' + secret_message[i:]
        print(secret_message)
    elif command[0] == "Reverse":
        find = secret_message.find(command[1])
        lenght = len(command[1])
        message = command[1]
        if find > -1:
            secret_message = secret_message[:find] + secret_message[find+lenght:] + message[::-1]
            print(secret_message)
        else:
            print("error")
    elif command[0] == "ChangeAll":
        secret_message = secret_message.replace(command[1], command[2])
        print(secret_message)
    command = input().split(":|:")

print(f"You have a new text message: {secret_message}")
