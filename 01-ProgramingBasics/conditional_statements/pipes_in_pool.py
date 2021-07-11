volume = int(input())
flow_of_pipe1 = int(input())
flow_of_pipe2 = int(input())
time = float(input())

first_pipe_for_time = flow_of_pipe1 * time
second_pipe_for_time = flow_of_pipe2 * time
total = first_pipe_for_time + second_pipe_for_time
percent = (total / volume) * 100
first_pipe_percent = (first_pipe_for_time / total) * 100
second_pipe_percent = (second_pipe_for_time / total) * 100

if percent <= 100:
    print(f"The pool is {percent:.2f}% full. Pipe 1: {first_pipe_percent:.2f}%. Pipe 2: {second_pipe_percent:.2f}%.")
else:
    difference = total - volume
    print(f"For {time:.2f} hours the pool overflows with {difference:.2f} liters.")