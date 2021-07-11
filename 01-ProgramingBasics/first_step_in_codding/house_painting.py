house_height = float(input())
house_width = float(input())
roof_height = float(input())

back_and_front_house_area = (2 * (house_height ** 2)) - (1.2 * 2)
side_house_area = (2 * (house_height * house_width)) - 2 * (1.5 ** 2)
green_paint_area = (back_and_front_house_area + side_house_area)
print(f'{green_paint_area / 3.4:.2f}')

roof_area = 2 * (house_width * house_height) + 2 * ((house_height/2) * roof_height)
print(f'{roof_area / 4.3:.2f}')