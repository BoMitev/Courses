import datetime

class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def int2mont(cls, month):
        month_str = datetime.date(1980, int(month), 1).strftime("%B")
        return month_str

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        month, year = cls.int2mont(date.split('.')[1]), int(date.split('.')[2])

        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age " \
               f"restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"