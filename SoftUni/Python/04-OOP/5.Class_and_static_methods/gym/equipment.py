class Equipment:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.get_next_id()

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"