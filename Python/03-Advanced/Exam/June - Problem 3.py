# Write a function called list_manipulator which receives a list of numbers as first parameter and different amount of other parameters. The second parameter might be "add" or "remove". The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
# •	In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers and return the new list
# •	In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
# •	In case of "remove" and "beginning"
# o	If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
# o	If there are no other parameters, remove only the first element of the list.
# o	Finaly, return the new list
# •	In case of "remove" and "end"
# o	If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
# o	Otherwise if there are no other parameters, remove only the last element of the list.
# o	Finaly, return the new list
# For more clarifications, see the examples below.


def list_manipulator(nums, command, *pos):
    if command == "add":
        if pos[0] == "beginning":
            return list(pos[1:]) + list(nums)
        elif pos[0] == "end":
            return list(nums) + list(pos[1:])
    elif command == "remove":
        if pos[0] == "beginning":
            if len(pos) > 1:
                i = pos[1]
                return nums[i:]
            return nums[1:]
        elif pos[0] == "end":
            if len(pos) > 1:
                i = pos[1]
                return nums[:-i]
            return nums[:-1]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
