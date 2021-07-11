a = old_a = input()
b = input()

a = b
b = old_a

print(f"Before:")
print(f"a = {old_a}")
print(f"b = {a}")
print(f"After:")
print(f"a = {a}")
print(f"b = {old_a}")