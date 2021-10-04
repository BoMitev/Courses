import warnings

numbers_dictionary = {}
line = input()
while line != "Search":
    number = input()
    if not number.isdigit():
        warnings.warn("The variable number must be an integer")
    elif line not in numbers_dictionary.keys():
        numbers_dictionary[line] = int(number)
    line = input()

searched_number = input()
while searched_number != "Remove":
    if searched_number not in numbers_dictionary.keys():
        warnings.warn("Number does not exist in dictionary")
    else:
        print(numbers_dictionary[searched_number])
    searched_number = input()

remove_number = input()
while remove_number != "End":
    if remove_number not in numbers_dictionary.keys():
        warnings.warn("Number does not exist in dictionary")
    else:
        numbers_dictionary.pop(remove_number)
    remove_number = input()

print(numbers_dictionary)
