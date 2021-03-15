record = float(input())
meters = float(input())
time_for_meter = float(input())

pure_time = meters * time_for_meter
resistance = (meters // 15) * 12.5
total_time = pure_time + resistance
difference = total_time - record

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")