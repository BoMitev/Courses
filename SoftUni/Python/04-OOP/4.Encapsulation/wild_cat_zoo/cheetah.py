from wild_cat_zoo.animal import Animal


class Cheetah(Animal):
    def __init__(self, name, age, gender, money_for_care=60):
        super().__init__(name, age, gender, money_for_care)
