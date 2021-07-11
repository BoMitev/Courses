lines = int(input())
opened_brackets = 0
closed_brackets = 0
is_balanced = True

for _ in range(lines):
    string = input()
    if string == "(":
        opened_brackets += 1
    elif string == ")":
        closed_brackets += 1

    if closed_brackets > opened_brackets:
        is_balanced = False
        break
    if opened_brackets - 1 > closed_brackets:
        is_balanced = False
        break
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")