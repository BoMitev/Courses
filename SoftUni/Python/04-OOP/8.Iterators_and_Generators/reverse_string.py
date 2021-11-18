def reverse_text(text):
    index = len(text) - 1
    reversed_text = ""
    while index >= 0:
        yield text[index]
        index -= 1

    return reversed_text


for char in reverse_text("step"):
    print(char, end='')
