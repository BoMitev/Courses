import os

path = os.getcwd()
desktop_path = os.path.expanduser("~/Desktop")
files = {}
for file in os.listdir(path):
    name, extension = file.split(".")
    if extension not in files.keys():
        files[extension] = []
    files[extension].append(file)

with open(desktop_path + "/report.txt", 'a') as text_file:
    for key, value in sorted(files.items(), key=lambda x: x[0]):
        text_file.write(f".{key}\n")
        for item in sorted(value):
            text_file.write(f"---{item}\n")