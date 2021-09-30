import os
if os.path.exists("my_first_file.txt"):
    os.remove("my_first_file.txt")
else:
    print("File already deleted!")