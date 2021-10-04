# Create a function called get_magic_triangle which will receive a single parameter (integer n) and it should create a magic triangle which follows those rules:
# •	We start with this simple triangle [[1], [1, 1]]
# •	We generate the next rows until we reach n amount of rows
# •	Each number in each row is equal to the sum of the two numbers right above it in the triangle
# •	If the current number has no neighbor to the upper left/rigth, we just take the existing neighbor
# After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5


def is_valid(row, col, n):
    return 0 <= row < n and 0 <= col <= row

def get_magic_triangle(n, triangle=[[1], [1, 1]]):
    for rows in range(2, n):
        row = []
        for col in range(rows + 1):
            num_1, num_2 = 0, 0
            if is_valid(rows-1, col-1, n):
                num_1 = triangle[rows-1][col-1]
            if is_valid(rows-1, col, n):
                num_2 = triangle[rows-1][col]
            row.append(num_1 + num_2)
        triangle.append(row)

    return triangle

get_magic_triangle(5)

