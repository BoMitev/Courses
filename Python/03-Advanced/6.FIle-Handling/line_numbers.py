import string
import os

def read_file(path):
    with open(path, 'r') as file:
        lines = file.read().split("\n")
        for line in range(len(lines)):
            count = 0
            letters = 0
            for char in lines[line]:
                if char.isalpha():
                    letters += 1
                elif char in string.punctuation:
                    count += 1
            lines[line] = f"Line {line+1}: {lines[line]} ({letters})({count})"

    with open("output.txt", 'w') as file:
        file.write('\n'.join(lines))


file_path = os.path.join(os.getcwd(), "", "text.txt")
read_file(file_path)