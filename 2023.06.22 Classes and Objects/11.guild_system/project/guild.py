class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, new_player):
        if new_player.guild == self.name:
            return f"Player {new_player.name} is already in the guild."
        elif new_player.guild != "Unaffiliated":
            return f"Player {new_player.name} is in another guild."
        new_player.guild = self.name
        self.players.append(new_player)
        return f"Welcome player {new_player.name} to the guild {self.name}"

    def kick_player(self, name):
        for player in self.players:
            if player.name == name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {name} has been removed from the guild."
        return f"Player {name} is not in the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}"]
        for player in self.players:
            result.append(player.player_info())
        return "\n".join(str(el) for el in result)