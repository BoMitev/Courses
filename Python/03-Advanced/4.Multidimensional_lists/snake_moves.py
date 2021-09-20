def read_matrix():
    rows, columns = map(int, input().split())
    text = list(input())
    index = 0
    matrix = []
    for r in range(rows):
        matrix.append([])
        for c in range(columns):
            matrix[r].append(text[index])
            index += 1
            if index >= len(text):
                index = 0
    return matrix, columns


matrix, columns = read_matrix()

for r in range(len(matrix)):
    if r % 2 == 1:
        print(''.join(matrix[r][::-1]))
    else:
        print(''.join(matrix[r]))