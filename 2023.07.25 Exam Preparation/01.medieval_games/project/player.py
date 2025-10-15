class Player:
    players = []

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        # self._need_sustenance = False
        self.stamina = stamina

        # if 0 <= self.stamina < 100:
        #     self._need_sustenance = True
        if not self.name:
            raise ValueError("Name not valid!")
        if self.name in Player.players:
            raise Exception(f"Name {self.name} is already used!")
        if self.age < 12:
            raise ValueError("The player cannot be under 12 years old!")
        if self.stamina < 0 or self.stamina > 100:
            raise ValueError("Stamina not valid!")

        Player.players.append(self.name)

    def need_sustenance(self):
        if self.stamina < 100:
            return True

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance()}"
