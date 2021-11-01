from wild_cat_zoo.animal import Animal


class Lion(Animal):
    def __init__(self, name, age, gender, money_for_care=50):
        super().__init__(name, age, gender, money_for_care)
