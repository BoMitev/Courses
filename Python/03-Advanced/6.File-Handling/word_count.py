import re


def get_file_content(path):
    with open(path, 'r') as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-z/']+", text.lower())

def write_result(result):
    with open("output.txt", 'w') as file:
        file.writelines("\n".join(result))
    return open('output.txt', 'r').read()

occurences = {}
path_words = "words.txt"
path_text = "text.txt"

first_file = get_file_content(path_words)
second_file = get_file_content(path_text)

for word in first_file:
    if word in second_file:
        occurences[word] = second_file.count(word)

result = [f"{el[0]} - {el[1]}" for el in sorted(occurences.items(), key=lambda x: -x[1])]

print(write_result(result))