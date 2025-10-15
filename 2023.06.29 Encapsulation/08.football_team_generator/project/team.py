class Team:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, name):
        for player in self.__players:
            if player.name == name:
                self.__players.remove(player)
                return player
        else:
            return f"Player {name} not found"
