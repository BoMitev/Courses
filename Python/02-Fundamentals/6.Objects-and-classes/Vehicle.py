class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, new_owner):
        if self.owner:
            return "Car already sold"
        elif self.price > money:
            return "Sorry, not enough money"
        else:
            self.owner = new_owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"

    def sell(self):
        if not self.owner:
            print("Vehicle has no owner")
        self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)

