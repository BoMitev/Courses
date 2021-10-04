import re
import os


def read_file(path):
    with open(path, 'r') as file:
        lines = file.read().split("\n")
        for line in range(len(lines)):
            if line % 2 == 0:
                text = re.sub(r'[-,.!?]', "@", lines[line])
                print(' '.join(text.split()[-1::-1]))


file_path = os.path.join(os.getcwd(), "", "text.txt")
read_file(file_path)