import math
player_one = int(input())
player_two = int(input())
player_tree = int(input())

total_time = player_one + player_two + player_tree
minutes = total_time / 60
seconds = total_time % 60
minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')