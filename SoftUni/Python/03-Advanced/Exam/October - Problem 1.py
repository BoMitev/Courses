# On the first line you will be given the jobs as integers (clock-cycles needed to finish the job) separated by comma
# and space ", ". On the second line you will be given the index of the job that we are interested in and want to know
# how many cycles will pass until the job is done.
# The tasks that need the least amount of clock-cycles will be completed first.
# For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
# You have to print how many clock-cycles will pass until the task you are interested in is completed. For more
# clarifications, see the examples below.

from operator import itemgetter

jobs = [int(x) for x in input().split(", ")]
index = int(input())
count = 0
jobs = list(enumerate(jobs))

for job in sorted(jobs, key=lambda x: x[1]):
    current_index = job[0]
    current_job = job[1]
    count += current_job
    if current_index == index:
        break

print(count)