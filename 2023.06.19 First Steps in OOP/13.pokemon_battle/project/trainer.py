# from pokemon import Pokemon
#

class Trainer:
    def __init__(self, name: str, pokemons=None):
        if pokemons is None:
            pokemons = []
        self.name = name
        self.pokemons = pokemons

    def add_pokemon(self, pokemon1):
        if pokemon1 not in self.pokemons:
            self.pokemons.append(pokemon1)
            return f"Caught {pokemon1.name} with health {pokemon1.health}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, name: str):
        for pokemon3 in self.pokemons:
            if pokemon3.name == name:
                self.pokemons.remove(pokemon3)
                return f"You have released {name}"
            else:
                continue
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for pokemon2 in self.pokemons:
            result.append(f"- {pokemon2.pokemon_details()}")
        return "\n".join(result)

# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
