num = int(input())
dictionary = {}

for _ in range(num):
    car, mileage, fuel = input().split("|")
    dictionary[car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input().split(" : ")
while command[0] != "Stop":
    car = command[1]
    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > dictionary[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            dictionary[car]["mileage"] += distance
            dictionary[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if dictionary[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                dictionary.pop(car)
    elif command[0] == "Refuel":
        fuel = int(command[2])
        if dictionary[car]["fuel"] + fuel <= 75:
            amount = fuel
        else:
            diff = (dictionary[car]["fuel"] + fuel) - 75
            amount = fuel - diff
        dictionary[car]["fuel"] += amount
        print(f"{car} refueled with {amount} liters")
    elif command[0] == "Revert":
        kilometers = int(command[2])
        if dictionary[car]["mileage"] - kilometers >= 10000:
            dictionary[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            dictionary[car]["mileage"] = 10000
    command = input().split(" : ")

for key, value in sorted(dictionary.items(), key=lambda x: (-x[1]['mileage'], x[0])):
    print(f"{key} -> Mileage: {dictionary[key]['mileage']} kms, Fuel in the tank: {dictionary[key]['fuel']} lt.")