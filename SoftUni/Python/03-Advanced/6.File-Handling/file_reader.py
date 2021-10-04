file = open('numbers.txt', 'r')

total = 0
line = [int(x[0]) for x in file.readlines()]
print(sum(line))

#the_sum = 0
#for line in file:
#   the_sum += int(line)

#print(the_sum)