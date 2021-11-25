import time
from random import randint

text = "".join(chr(randint(35, 195)) for _ in range(1024 * 1024))


def reverse_text_slow(string: str):
    return (ch for ch in reversed(string))


def reverse_text_fast(string: str):
    for index in range(len(string) - 1, -1, -1):
        yield string[index]


start = time.time()
result = ""
for char in reverse_text_slow(text):
    result += char
end = time.time()
slow_time = end - start

start = time.time()
result = ""
for char in reverse_text_slow(text):
    result += char
end = time.time()
fast_time = end - start

print(f"Slow function time: {slow_time}")
print(f"Fast function time: {fast_time}")