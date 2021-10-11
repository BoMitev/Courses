from fibonacci_sequence import create_sequence, locate

command = input()
while command != "Stop":
    commands = command.split()
    num = int(commands[-1])

    if "Create" in commands:
        print(create_sequence(num))

    elif "Locate" in commands:
        try:
            print(locate(num))
        except IndexError as err:
            print(err)

    command = input()