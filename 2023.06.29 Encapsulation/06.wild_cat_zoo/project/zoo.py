class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.capacity = workers_capacity
        self.animals = []
        self.workers = []
        self.salaries = 0
        self.animals_pay = 0
        self.lions = []
        self.tigers = []
        self.cheetahs = []
        self.keepers = []
        self.caretakers = []
        self.vets = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value

    def add_animal(self, animal, price):
        if (self.animal_capacity - 1 >= 0) and (self.budget - price < 0):
            return "Not enough budget"
        elif self.animal_capacity - 1 < 0:
            return "Not enough space for animal"

        self.animal_capacity -= 1
        self.budget -= price
        self.animals_pay += animal.money_for_care
        self.animals.append(animal)

        if type(animal).__name__ == "Lion":
            self.lions.append(animal)
        elif type(animal).__name__ == "Tiger":
            self.tigers.append(animal)
        elif type(animal).__name__ == "Cheetah":
            self.cheetahs.append(animal)

        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.capacity - 1 < 0:
            return "Not enough space for worker"

        self.capacity -= 1
        self.workers.append(worker)
        self.salaries += worker.salary

        if type(worker).__name__ == "Keeper":
            self.keepers.append(worker)
        elif type(worker).__name__ == "Caretaker":
            self.caretakers.append(worker)
        elif type(worker).__name__ == "Vet":
            self.vets.append(worker)

        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, name):
        for worker in self.workers:
            if worker.name == name:
                self.workers.remove(worker)
                if type(worker).__name__ == "Keeper":
                    self.keepers.remove(worker)
                elif type(worker).__name__ == "Caretaker":
                    self.caretakers.remove(worker)
                elif type(worker).__name__ == "Vet":
                    self.vets.remove(worker)
                return f"{worker.name} fired successfully"
        else:
            return f"There is no {name} in the zoo"

    def pay_workers(self):
        if self.budget - self.salaries < 0:
            return "You have no budget to pay your workers. They are unhappy"

        self.budget -= self.salaries
        return f"You payed your workers. They are happy. Budget left: {self.budget}"

    def tend_animals(self):
        if self.budget - self.animals_pay < 0:
            return "You have no budget to tend the animals. They are unhappy."

        self.budget -= self.animals_pay
        return f"You tended all the animals. They are happy. Budget left: {self.budget}"

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals", f"----- {len(self.lions)} Lions:"]
        for lion in self.lions:
            result.append(f"{lion.__repr__()}")

        result.append(f"----- {len(self.tigers)} Tigers:")
        for tiger in self.tigers:
            result.append(f"{tiger.__repr__()}")

        result.append(f"----- {len(self.cheetahs)} Cheetahs:")
        for cheetah in self.cheetahs:
            result.append(f"{cheetah.__repr__()}")

        return "\n".join(str(el) for el in result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers", f"----- {len(self.keepers)} Keepers:"]
        for keeper in self.keepers:
            result.append(f"{keeper.__repr__()}")

        result.append(f"----- {len(self.caretakers)} Caretakers:")
        for caretaker in self.caretakers:
            result.append(f"{caretaker.__repr__()}")

        result.append(f"----- {len(self.vets)} Vets:")
        for vet in self.vets:
            result.append(f"{vet.__repr__()}")

        return "\n".join(str(el) for el in result)
