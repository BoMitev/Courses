vegetable_price = float(input())
fruit_price = float(input())
vegetable_kilos = int(input())
fruit_kilos = int(input())

vegetable_profit = (vegetable_price * vegetable_kilos) / 1.94
fruit_profit = (fruit_price * fruit_kilos) / 1.94
profit = vegetable_profit + fruit_profit
print(f'{profit:.2f}')