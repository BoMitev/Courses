type_fire = input().split("#")
amount_of_water = int(input())
effors = 0
total_fire = 0
valid_cells = []
for x in range(len(type_fire)):
    fire_cell = type_fire[x].split(" = ")
    if amount_of_water > 0:
        if fire_cell[0] == "High" and 81 <= int(fire_cell[1]) <= 125:
            if amount_of_water >= int(fire_cell[1]):
                amount_of_water -= int(fire_cell[1])
            else:
                continue
            effors += 0.25 * int(fire_cell[1])
            total_fire += int(fire_cell[1])
            valid_cells.append(fire_cell[1])
        elif fire_cell[0] == "Medium" and 51 <= int(fire_cell[1]) <= 80:
            if amount_of_water >= int(fire_cell[1]):
                amount_of_water -= int(fire_cell[1])
            else:
                continue
            effors += 0.25 * int(fire_cell[1])
            total_fire += int(fire_cell[1])
            valid_cells.append(fire_cell[1])
        elif fire_cell[0] == "Low" and 1 <= int(fire_cell[1]) <= 50:
            if amount_of_water >= int(fire_cell[1]):
                amount_of_water -= int(fire_cell[1])
            else:
                continue
            effors += 0.25 * int(fire_cell[1])
            total_fire += int(fire_cell[1])
            valid_cells.append(fire_cell[1])
    else:
        break

print("Cells:")
for cell in valid_cells:
    print(f" - {cell}")
print(f"Effort: {effors:.2f}")
print(f"Total Fire: {total_fire}")
