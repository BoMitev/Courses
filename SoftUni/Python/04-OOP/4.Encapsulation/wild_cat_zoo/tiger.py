from wild_cat_zoo.animal import Animal


class Tiger(Animal):
    def __init__(self, name, age, gender, money_for_care=45):
        super().__init__(name, age, gender, money_for_care)
        