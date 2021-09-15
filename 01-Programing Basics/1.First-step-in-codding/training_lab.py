width = float(input())
height = float(input())

if 3 <= height <= width <= 100:
    height *= 100
    width *= 100
    places_per_row = (height-100) // 70
    rows = width // 120
    places = places_per_row * rows - 3
    print(places)
else:
    print('Not enough space')