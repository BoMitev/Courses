n = int(input())
longest = set()

for _ in range(n):
    data = input().split("-")
    first_start = int(data[0].split(",")[0])
    first_end = int(data[0].split(",")[1])
    second_start = int(data[1].split(",")[0])
    second_end = int(data[1].split(",")[1])
    first_set = set(x for x in range(first_start, first_end+1))
    second_set = set(x for x in range(second_start, second_end+1))
    intersection = tuple(first_set.intersection(second_set))
    if len(longest) < len(intersection):
        longest = intersection

longest = [str(x) for x in longest]
print(f"Longest intersection is [{', '.join(longest)}] with length {len(longest)}")