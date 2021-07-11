type_of_fuel = input()
volume = float(input())

if type_of_fuel == "Diesel" or type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
    if volume >= 25:
        print(f"You have enough {type_of_fuel.lower()}.")
    elif volume < 25:
        print(f"Fill your tank with {type_of_fuel.lower()}!")
else:
    print("Invalid fuel!")