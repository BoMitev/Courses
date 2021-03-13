number_of_balls = balls = int(input())
points = 0
list_colors = []

while 0 < balls:
    color = input()
    list_colors.append(color)
    if color == "red":
        points += 5
    elif color == "orange":
        points += 10
    elif color == "yellow":
        points += 15
    elif color == "white":
        points += 20
    elif color == "black":
        points /= 2
    else:
        points += 0

    balls -= 1

red_count = list_colors.count('red')
orange_count = list_colors.count('orange')
yellow_count = list_colors.count('yellow')
white_count = list_colors.count('white')
black_count = list_colors.count('black')
total = red_count + orange_count + yellow_count + white_count + black_count

print(f'Total points: {int(points)}\n'
      f'Points from red balls: {red_count}\n'
      f'Points from orange balls: {orange_count}\n'
      f'Points from yellow balls: {yellow_count}\n'
      f'Points from white balls: {white_count}\n'
      f'Other colors picked: {number_of_balls - total}\n'
      f'Divides from black balls: {black_count}')
