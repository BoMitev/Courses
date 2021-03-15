travel_expenses = float(input())
puzzles = int(input())
teddy = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = 2.6
teddy_price = 3
bears_price = 4.1
minions_price = 8.2
trucks_price = 2
final_prize = (puzzles * puzzles_price + teddy * teddy_price +
               bears * bears_price + minions * minions_price +
               trucks * trucks_price)
total_pcs = puzzles + teddy + bears + minions + trucks
if total_pcs >= 50:
    final_prize *= 0.75
profit = final_prize * 0.9
difference = abs(travel_expenses - profit)
if travel_expenses <= profit:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
