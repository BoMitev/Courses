joinery_pcs = int(input())
type_joinery = input()
delivery = input()
delivery_price = 0
joinery_price = 0

if type_joinery == "90X130":
    joinery_price = 110
    if joinery_pcs > 60:
        joinery_price *= 0.92
    elif joinery_pcs > 30:
        joinery_price *= 0.95
elif type_joinery == "100X150":
    joinery_price = 140
    if joinery_pcs > 80:
        joinery_price *= 0.90
    elif joinery_pcs > 40:
        joinery_price *= 0.94
elif type_joinery == "130X180":
    joinery_price = 190
    if joinery_pcs > 50:
        joinery_price *= 0.88
    elif joinery_pcs > 20:
        joinery_price *= 0.93
elif type_joinery == "200X300":
    joinery_price = 250
    if joinery_pcs > 50:
        joinery_price *= 0.86
    elif 25 <= joinery_pcs > 25:
        joinery_price *= 0.91

if delivery == "With delivery":
    delivery_price = 60

total_price = (joinery_price * joinery_pcs) + delivery_price

if joinery_pcs < 10:
    print('Invalid order')
elif 10 < joinery_pcs <= 99:
    print(f"{total_price:.2f} BGN")
else:
    print(f"{total_price * 0.96:.2f} BGN")
