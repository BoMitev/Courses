first = input()
second = input()
last_string = first
for symbol in range(len(first)):
    left_part = second[:symbol+1]
    right_part = first[symbol+1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string
