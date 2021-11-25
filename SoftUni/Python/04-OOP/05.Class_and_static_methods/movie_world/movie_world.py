class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return cls.DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls.CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if MovieWorld.CUSTOMER_CAPACITY > len(self.customers):
            self.customers.append(customer)
            return True
        return False

    def add_dvd(self, dvd):
        if MovieWorld.DVD_CAPACITY > len(self.dvds):
            self.dvds.append(dvd)
            return True
        return False

    def rent_dvd(self, customer_id, dvd_id):
        dvd = [d for d in self.dvds if dvd_id == d.id][0]
        customer = [c for c in self.customers if customer_id == c.id][0]

        if dvd.id in [d.id for d in customer.rented_dvds]:
            return f"{customer.name} has already rented {dvd.name}"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        if dvd.is_rented:
            return "DVD is already rented"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        info = [c.__repr__() for c in self.customers]
        info.extend([d.__repr__() for d in self.dvds])
        return '\n'.join(info)
