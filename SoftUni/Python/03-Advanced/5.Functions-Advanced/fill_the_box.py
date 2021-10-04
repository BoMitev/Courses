def fill_the_box(height, length, width, *args, space=None):
    args = list(args)
    if space is None:
        space = height * length * width

    if args[0] == "Finish":
        return f"There is free space in the box. You could put {space} more cubes."
    elif space - args[0] <= 0:
        args[0] -= space
        return f"No more free space! You have {sum(args[:-1])} more cubes."
        pass

    return fill_the_box(height, length, width, *args[1:], space= space - args[0])


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))