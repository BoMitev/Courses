activation_key = input()

while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        break
    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        string = activation_key[start_index:end_index]
        if command[1] == "Upper":
            activation_key = activation_key[:start_index] + string.upper() + activation_key[end_index:]
        elif command[1] == "Lower":
            activation_key = activation_key[:start_index] + string.lower() + activation_key[end_index:]
        print(activation_key)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
print(f"Your activation key is: {activation_key}")