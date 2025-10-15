class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(name=f"{self.name} {other.name}", people=self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([str(el) for el in self.people])}"

    def __str__(self):
        return f"Group {self.name} with members {', '.join([str(el) for el in self.people])}"

    def __getitem__(self, idx):
        return f"Person {idx}: {str(self.people[idx])}"

    def __iter__(self):
        for idx in range(len(self.people)):
            yield f"Person {idx}: {self.people[idx].__repr__()}"
