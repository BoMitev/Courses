class Trainer:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.get_next_id()

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
