kilometers = int(input())
time = input()

taxi_start_price = 0.7
taxi_day_tax = 0.79
taxi_night_tax = 0.9
bus_tax = 0.09
train_tax = 0.06

if kilometers >= 100:
    price = train_tax * kilometers
    print(f"{price:.2f}")
elif kilometers >= 20:
    price = bus_tax * kilometers
    print(f"{price:.2f}")
elif time == "day":
        price = taxi_start_price + (taxi_day_tax * kilometers)
        print(f"{price:.2f}")
elif time == "night":
        price = taxi_start_price + (taxi_night_tax * kilometers)
        print(f"{price:.2f}")
