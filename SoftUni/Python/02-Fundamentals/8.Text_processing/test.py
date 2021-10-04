string_line = input()
start = 0
result_string = ""

list_with_unique_chars = []

for index in range(len(string_line)):
    char = string_line[index]
    if char.isdigit():
        its_index = string_line.find(char)
        result_string += string_line[start:its_index].upper() * int(string_line[its_index])
        start = its_index + 1
    else:
        if char.upper() not in list_with_unique_chars:
            list_with_unique_chars.append(char.upper())

print(f"Unique symbols used: {len(list_with_unique_chars)}")
print(result_string)