command = input()
coffee_counter = 0

while command != "END":
    if command == "dog" or command == "cat" or command == "coding" or command == "movie":
        coffee_counter += 1
    elif command == "DOG" or command == "CAT" or command == "CODING" or command == "MOVIE":
        coffee_counter += 2
    command = input()

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)