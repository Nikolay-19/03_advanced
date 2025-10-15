from project.player import Player
from project.supply.food import Food
from project.supply.drink import Drink


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        current = []
        for arg in args:
            if arg not in self.players:
                current.append(arg)
                self.players.append(arg)
        try:
            return f"Successfully added: {', '.join(str(el.name) for el in current)}"
        except Exception:
            return f"Successfully added: "

    def add_supply(self, *args):
        for arg in args:
            self.supplies.append(arg)

    def find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def find_supply(self, supply_type):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)

    def sustain(self, player_name, sustenance_type):
        player = self.find_player(player_name)
        if not player.need_sustenance():
            return f"{player.name} have enough stamina."
        supply = self.find_supply(sustenance_type)

        if not supply:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina += supply.energy
        if player.stamina > 100:
            player.stamina = 100

        return f"{player.name} sustained successfully with {supply.name}."

    @staticmethod
    def check_zero_stamina(player_1, player_2):
        if player_1.stamina < 0:
            player_1.stamina = 0
            return f"Winner: {player_2.name}"
        if player_2.stamina < 0:
            player_2.stamina = 0
            return f"Winner: {player_1.name}"

    @staticmethod
    def check_winner(player_1, player_2):
        if player_1.stamina > player_2.stamina:
            return f"Winner: {player_1.name}"
        else:
            return f"Winner: {player_2.name}"

    @staticmethod
    def attack(player_1, player_2):
        player_2.stamina -= (player_1.stamina / 2)

    def duel(self, first_player_name, second_player_name):
        player_1 = self.find_player(first_player_name)
        player_2 = self.find_player(second_player_name)

        if player_1.stamina == 0 and player_2.stamina == 0:
            return (f"Player {player_1.name} does not have enough stamina.\n"
                    f"Player {player_2.name} does not have enough stamina.")
        if player_1.stamina == 0:
            return f"Player {player_1.name} does not have enough stamina."
        if player_2.stamina == 0:
            return f"Player {player_2.name} does not have enough stamina."

        if player_1.stamina < player_2.stamina:
            self.attack(player_1, player_2)
            self.check_zero_stamina(player_1, player_2)
            self.attack(player_2, player_1)
            self.check_zero_stamina(player_1, player_2)
        else:
            self.attack(player_2, player_1)
            self.check_zero_stamina(player_1, player_2)
            self.attack(player_1, player_2)
            self.check_zero_stamina(player_1, player_2)

        return self.check_winner(player_1, player_2)

    def reduce_stamina(self):
        for player in self.players:
            player.stamina -= (player.age * 2)
            if player.stamina < 0:
                player.stamina = 0

    def next_day(self):
        self.reduce_stamina()
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance()}")
        for supply in self.supplies:
            result.append(f"{type(supply).__name__}: {supply.name}, {supply.energy}")

        return "\n".join(str(el) for el in result)


controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)
