class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price:
            if self.__animal_capacity > len(self.animals):
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            return "Not enough space for animal"
        return "Not enough budget"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total = 0
        for worker in self.workers:
            total += worker.salary
        if self.__budget >= total:
            self.__budget -= total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total = 0
        for animal in self.animals:
            total += animal.money_for_care
        if self.__budget >= total:
            self.__budget -= total
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions, tigers, cheetahs = [], [], []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal.__repr__())
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal.__repr__())
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal.__repr__())

        info = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"] + lions +\
            [f"----- {len(tigers)} Tigers:"] + tigers + [f"----- {len(cheetahs)} Cheetahs:"] + cheetahs

        return '\n'.join(info)

    def workers_status(self):
        keepers, caretakers, vets = [], [], []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker.__repr__())
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker.__repr__())
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker.__repr__())

        info = [f"You have {len(self.workers)} workers", f'----- {len(keepers)} Keepers:'] + keepers +\
            [f"----- {len(caretakers)} Caretakers:"] + caretakers + [f'----- {len(vets)} Vets:'] + vets

        return '\n'.join(info)
