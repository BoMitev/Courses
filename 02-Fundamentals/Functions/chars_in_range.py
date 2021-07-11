def char_range(num_1, num_2):
    for i in range(num_1 + 1, num_2):
        print(chr(i), end=" ")

char_1 = ord(input())
char_2 = ord(input())

char_range(char_1, char_2)