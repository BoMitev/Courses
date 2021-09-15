num = int(input())
dictionary = {}

for _ in range(num):
    piece, composer, key = input().split("|")
    dictionary[piece] = {composer: key}

command = input().split("|")
while command[0] != "Stop":
    piece = command[1]
    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if piece not in dictionary.keys():
            dictionary[piece] = {composer:key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        if piece in dictionary.keys():
            dictionary.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        new_key = command[2]
        if piece in dictionary.keys():
            for v in dictionary[piece].keys():
                dictionary[piece][v] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input().split("|")

for key,value in sorted(dictionary.items()):
    for k,v in sorted(value.items()):
        print(f"{key} -> Composer: {k}, Key: {v}")