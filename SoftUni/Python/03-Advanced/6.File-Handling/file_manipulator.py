import os

path = os.getcwd()
while True:
    command = input().split("-")
    if command[0] == "End":
        break
    file_name = path+command[1]
    print(file_name)
    if command[0] == "Create":
        open(file_name, 'w').close()
    elif command[0] == "Add":
        content = command[2]
        with open(file_name, 'a') as file:
            file.write(f"{content}\n")
    elif command[0] == "Replace":
        old_string = command[2]
        new_string = command[3]
        try:
            with open(file_name, 'r') as file:
                content = ""
                for line in file:
                    content += line.replace(old_string, new_string)
            writing_file = open(file_name, 'w')
            writing_file.write(content)
            writing_file.close()
        except FileNotFoundError:
            print("An error occurred")
    elif command[0] == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")