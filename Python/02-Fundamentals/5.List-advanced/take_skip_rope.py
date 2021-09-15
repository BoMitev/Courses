message = input()
num_list = [x for x in message if x.isdigit()]
non_num_list = [x for x in message if not x.isdigit()]
alpha = "".join(non_num_list)
take_list = [num_list[x] for x in range(len(num_list)) if x % 2 == 0]
skip_list = [num_list[x] for x in range(len(num_list)) if x % 2 == 1]
result = ""
for i in range(len(take_list)):
    take = int(take_list[i])
    skip = int(skip_list[i])
    result += alpha[:take]
    skipped = alpha[:take+skip]
    alpha = alpha[len(skipped):]
print(result)